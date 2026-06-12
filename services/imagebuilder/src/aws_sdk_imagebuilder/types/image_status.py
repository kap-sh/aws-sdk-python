"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ImageStatus: TypeAlias = Literal[
    "PENDING",
    "CREATING",
    "BUILDING",
    "TESTING",
    "DISTRIBUTING",
    "INTEGRATING",
    "AVAILABLE",
    "CANCELLED",
    "FAILED",
    "DEPRECATED",
    "DELETED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "CREATING",
        "BUILDING",
        "TESTING",
        "DISTRIBUTING",
        "INTEGRATING",
        "AVAILABLE",
        "CANCELLED",
        "FAILED",
        "DEPRECATED",
        "DELETED",
        "DISABLED",
    )
)


def serialize_json(value: ImageStatus) -> str:
    return value


def deserialize_json(data: str) -> ImageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageStatus value: {data!r}")
    return cast(ImageStatus, data)
