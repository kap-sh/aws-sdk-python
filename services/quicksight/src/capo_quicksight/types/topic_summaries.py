"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_summary

TopicSummaries: TypeAlias = list["capo_quicksight.types.topic_summary.TopicSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: TopicSummaries) -> list:
    import capo_quicksight.types.topic_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicSummaries:
    import capo_quicksight.types.topic_summary

    out: TopicSummaries = []
    for item in data:
        out.append(capo_quicksight.types.topic_summary.deserialize_json(item))
    return out
