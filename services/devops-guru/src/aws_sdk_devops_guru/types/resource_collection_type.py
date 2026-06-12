"""Generated from Smithy shape ``com.amazonaws.devopsguru#ResourceCollectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

ResourceCollectionType: TypeAlias = Literal[
    "AWS_CLOUD_FORMATION",
    "AWS_SERVICE",
    "AWS_TAGS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_CLOUD_FORMATION",
        "AWS_SERVICE",
        "AWS_TAGS",
    )
)


def serialize_json(value: ResourceCollectionType) -> str:
    return value


def deserialize_json(data: str) -> ResourceCollectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceCollectionType value: {data!r}")
    return cast(ResourceCollectionType, data)
