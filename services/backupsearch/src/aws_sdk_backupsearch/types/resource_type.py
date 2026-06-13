"""Generated from Smithy shape ``com.amazonaws.backupsearch#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backupsearch.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "S3",
    "EBS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "EBS",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
