"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_filter

TopicFilters: TypeAlias = list["capo_quicksight.types.topic_filter.TopicFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: TopicFilters) -> list:
    import capo_quicksight.types.topic_filter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicFilters:
    import capo_quicksight.types.topic_filter

    out: TopicFilters = []
    for item in data:
        out.append(capo_quicksight.types.topic_filter.deserialize_json(item))
    return out
