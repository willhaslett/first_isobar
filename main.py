import isobar as iso
import logging

from isobar.pattern import sequence

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

ride = iso.PSequence([48, 50])
ride = iso.PLoop(ride)

boom_chick = iso.PSequence([36, 38])
boom_chick = iso.PLoop(boom_chick)

timeline = iso.Timeline(85)
timeline.schedule({
  'note': ride,
  'duration': 0.5,
  'amplitude': 80
})
timeline.schedule({
  'note': boom_chick,
  'duration': 1,
  'amplitude': 80
})

timeline.run()