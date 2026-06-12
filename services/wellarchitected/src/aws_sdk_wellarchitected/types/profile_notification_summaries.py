"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileNotificationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_notification_summary

ProfileNotificationSummaries: TypeAlias = list[
    "aws_sdk_wellarchitected.types.profile_notification_summary.ProfileNotificationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileNotificationSummaries) -> list:
    import aws_sdk_wellarchitected.types.profile_notification_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wellarchitected.types.profile_notification_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProfileNotificationSummaries:
    import aws_sdk_wellarchitected.types.profile_notification_summary

    out: ProfileNotificationSummaries = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.profile_notification_summary.deserialize_json(
                item
            )
        )
    return out
