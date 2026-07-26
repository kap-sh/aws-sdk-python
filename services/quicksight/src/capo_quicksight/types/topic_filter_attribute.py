"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicFilterAttribute``."""

from typing import Literal, TypeAlias, cast

TopicFilterAttribute: TypeAlias = Literal[
    "QUICKSIGHT_USER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "TOPIC_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> TopicFilterAttribute:
    return cast(TopicFilterAttribute, data)
