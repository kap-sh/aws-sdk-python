"""Generated from Smithy shape ``com.amazonaws.rbin#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rbin.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "EBS_SNAPSHOT",
    "EC2_IMAGE",
    "EBS_VOLUME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EBS_SNAPSHOT",
        "EC2_IMAGE",
        "EBS_VOLUME",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
