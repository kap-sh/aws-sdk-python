"""Generated from Smithy shape ``com.amazonaws.notifications#StatusSummaryByRegion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_notifications.types.event_rule_status_summary
    import aws_sdk_notifications.types.region

StatusSummaryByRegion: TypeAlias = dict[
    "aws_sdk_notifications.types.region.Region",
    "aws_sdk_notifications.types.event_rule_status_summary.EventRuleStatusSummary",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StatusSummaryByRegion) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_notifications.types.event_rule_status_summary

        out[key] = aws_sdk_notifications.types.event_rule_status_summary.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> StatusSummaryByRegion:
    out: StatusSummaryByRegion = {}
    for key, value in data.items():
        import aws_sdk_notifications.types.event_rule_status_summary

        out[key] = (
            aws_sdk_notifications.types.event_rule_status_summary.deserialize_json(
                value
            )
        )
    return out
