"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "QUICKSIGHT_USER",
        "QUICKSIGHT_VIEWER_OR_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
        "QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "TOPIC_NAME",
    )
)


def serialize_json(value: TopicFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> TopicFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopicFilterAttribute value: {data!r}")
    return cast(TopicFilterAttribute, data)
