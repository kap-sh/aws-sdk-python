"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfPrefetchSchedule``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.prefetch_schedule

__listOfPrefetchSchedule: TypeAlias = list[
    "aws_sdk_mediatailor.types.prefetch_schedule.PrefetchSchedule"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPrefetchSchedule) -> list:
    import aws_sdk_mediatailor.types.prefetch_schedule

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.prefetch_schedule.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPrefetchSchedule:
    import aws_sdk_mediatailor.types.prefetch_schedule

    out: __listOfPrefetchSchedule = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.prefetch_schedule.deserialize_json(item))
    return out
