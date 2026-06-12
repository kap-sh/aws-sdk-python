"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#EventTypeBatch``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.event_type_summary

EventTypeBatch: TypeAlias = list[
    "aws_sdk_codestar_notifications.types.event_type_summary.EventTypeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventTypeBatch) -> list:
    import aws_sdk_codestar_notifications.types.event_type_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codestar_notifications.types.event_type_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EventTypeBatch:
    import aws_sdk_codestar_notifications.types.event_type_summary

    out: EventTypeBatch = []
    for item in data:
        out.append(
            aws_sdk_codestar_notifications.types.event_type_summary.deserialize_json(
                item
            )
        )
    return out
