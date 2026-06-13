"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicSearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_search_filter

TopicSearchFilterList: TypeAlias = list[
    "aws_sdk_quicksight.types.topic_search_filter.TopicSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicSearchFilterList) -> list:
    import aws_sdk_quicksight.types.topic_search_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.topic_search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicSearchFilterList:
    import aws_sdk_quicksight.types.topic_search_filter

    out: TopicSearchFilterList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.topic_search_filter.deserialize_json(item))
    return out
