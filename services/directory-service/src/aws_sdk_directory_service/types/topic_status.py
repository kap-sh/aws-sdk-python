"""Generated from Smithy shape ``com.amazonaws.directoryservice#TopicStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

TopicStatus: TypeAlias = Literal[
    "Registered",
    "Topic not found",
    "Failed",
    "Deleted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Registered",
        "Topic not found",
        "Failed",
        "Deleted",
    )
)


def serialize_aws_json_1_1(value: TopicStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TopicStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopicStatus value: {data!r}")
    return cast(TopicStatus, data)
