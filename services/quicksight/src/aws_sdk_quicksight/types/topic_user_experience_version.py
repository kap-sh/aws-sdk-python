"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicUserExperienceVersion``."""

from typing import Literal, TypeAlias, cast

TopicUserExperienceVersion: TypeAlias = Literal[
    "LEGACY",
    "NEW_READER_EXPERIENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicUserExperienceVersion) -> str:
    return value


def deserialize_json(data: str) -> TopicUserExperienceVersion:
    return cast(TopicUserExperienceVersion, data)
