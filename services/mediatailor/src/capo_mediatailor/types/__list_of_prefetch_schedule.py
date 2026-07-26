"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfPrefetchSchedule``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.prefetch_schedule

__listOfPrefetchSchedule: TypeAlias = list[
    "capo_mediatailor.types.prefetch_schedule.PrefetchSchedule"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPrefetchSchedule) -> list:
    import capo_mediatailor.types.prefetch_schedule

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.prefetch_schedule.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPrefetchSchedule:
    import capo_mediatailor.types.prefetch_schedule

    out: __listOfPrefetchSchedule = []
    for item in data:
        out.append(capo_mediatailor.types.prefetch_schedule.deserialize_json(item))
    return out
