from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration

import django

def passcard_info_view(request, passcode):
    # Получить список всех визитов по конкретному пропуску

    all_passcard_visits = []

    passcard_1  = Passcard.objects.filter(passcode = passcode ).get()
    visits  = Visit.objects.filter(passcard=passcard_1)
    for visit in visits:
      entered_at = django.utils.timezone.localtime(visit.entered_at)
      entered_at_str = entered_at.strftime("%d-%m-%Y %H:%M")

      sec = visit.get_duration()
      str_delta_time_visit = format_duration(sec)
      is_long_visit = visit.is_visit_long()

      one_record = {
            "entered_at": entered_at_str,
            "duration": str_delta_time_visit,
            "is_strange": is_long_visit,
      }
      all_passcard_visits.append(one_record)

    context = {
        "passcard": passcard_1,
        "this_passcard_visits": all_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
