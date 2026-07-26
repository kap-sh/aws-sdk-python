"""Generated from Smithy shape ``com.amazonaws.notifications#StatusSummaryByRegion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.event_rule_status_summary
    import capo_notifications.types.region

StatusSummaryByRegion: TypeAlias = dict[
    "capo_notifications.types.region.Region",
    "capo_notifications.types.event_rule_status_summary.EventRuleStatusSummary",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StatusSummaryByRegion) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_notifications.types.event_rule_status_summary

        out[key] = capo_notifications.types.event_rule_status_summary.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> StatusSummaryByRegion:
    out: StatusSummaryByRegion = {}
    for key, value in data.items():
        import capo_notifications.types.event_rule_status_summary

        out[key] = capo_notifications.types.event_rule_status_summary.deserialize_json(
            value
        )
    return out
