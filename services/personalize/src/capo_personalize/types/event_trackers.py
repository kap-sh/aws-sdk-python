"""Generated from Smithy shape ``com.amazonaws.personalize#EventTrackers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.event_tracker_summary

EventTrackers: TypeAlias = list[
    "capo_personalize.types.event_tracker_summary.EventTrackerSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTrackers) -> list:
    import capo_personalize.types.event_tracker_summary

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.event_tracker_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventTrackers:
    import capo_personalize.types.event_tracker_summary

    out: EventTrackers = []
    for item in data:
        out.append(
            capo_personalize.types.event_tracker_summary.deserialize_aws_json_1_1(item)
        )
    return out
