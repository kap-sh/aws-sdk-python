"""Generated from Smithy shape ``com.amazonaws.wellarchitected#NotificationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.notification_summary

NotificationSummaries: TypeAlias = list[
    "aws_sdk_wellarchitected.types.notification_summary.NotificationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSummaries) -> list:
    import aws_sdk_wellarchitected.types.notification_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wellarchitected.types.notification_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationSummaries:
    import aws_sdk_wellarchitected.types.notification_summary

    out: NotificationSummaries = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.notification_summary.deserialize_json(item)
        )
    return out
