"""Generated from Smithy shape ``com.amazonaws.applicationsignals#LatestChangeEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.change_event

LatestChangeEvents: TypeAlias = list[
    "aws_sdk_application_signals.types.change_event.ChangeEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: LatestChangeEvents) -> list:
    import aws_sdk_application_signals.types.change_event

    out: list = []
    for item in value:
        out.append(aws_sdk_application_signals.types.change_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> LatestChangeEvents:
    import aws_sdk_application_signals.types.change_event

    out: LatestChangeEvents = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.change_event.deserialize_json(item)
        )
    return out
