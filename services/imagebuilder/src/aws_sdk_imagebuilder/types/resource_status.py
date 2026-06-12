"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ResourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DELETED",
    "DEPRECATED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "DELETED",
        "DEPRECATED",
        "DISABLED",
    )
)


def serialize_json(value: ResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceStatus value: {data!r}")
    return cast(ResourceStatus, data)
