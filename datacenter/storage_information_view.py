from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render
import django


def storage_information_view(request):
    # Получить список всех визитов кто сейчас в хранилище
    visits  = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits:
      passcard_0 = visit.passcard
      entered_at = django.utils.timezone.localtime(visit.entered_at)
      entered_at_str = entered_at.strftime("%d-%m-%Y %H:%M")
      sec = visit.get_duration()

      str_delta_time_visit = format_duration(sec)
      is_long_visit = visit.is_visit_long()

      one_record = {
            "who_entered": passcard_0.owner_name,
            "entered_at": entered_at_str,
            "duration": str_delta_time_visit,
            "is_strange": is_long_visit,
      }
      non_closed_visits.append(one_record)

    context = {
        "non_closed_visits": non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
