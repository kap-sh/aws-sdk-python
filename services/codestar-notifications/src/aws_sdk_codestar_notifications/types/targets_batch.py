"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#TargetsBatch``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.target_summary

TargetsBatch: TypeAlias = list[
    "aws_sdk_codestar_notifications.types.target_summary.TargetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetsBatch) -> list:
    import aws_sdk_codestar_notifications.types.target_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codestar_notifications.types.target_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TargetsBatch:
    import aws_sdk_codestar_notifications.types.target_summary

    out: TargetsBatch = []
    for item in data:
        out.append(
            aws_sdk_codestar_notifications.types.target_summary.deserialize_json(item)
        )
    return out
