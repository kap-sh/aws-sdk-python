"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicUserExperienceVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopicUserExperienceVersion: TypeAlias = Literal[
    "LEGACY",
    "NEW_READER_EXPERIENCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEGACY",
        "NEW_READER_EXPERIENCE",
    )
)


def serialize_json(value: TopicUserExperienceVersion) -> str:
    return value


def deserialize_json(data: str) -> TopicUserExperienceVersion:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TopicUserExperienceVersion value: {data!r}"
        )
    return cast(TopicUserExperienceVersion, data)
