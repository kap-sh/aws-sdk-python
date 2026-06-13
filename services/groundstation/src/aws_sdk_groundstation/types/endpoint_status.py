"""Generated from Smithy shape ``com.amazonaws.groundstation#EndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

EndpointStatus: TypeAlias = Literal[
    "created",
    "creating",
    "deleted",
    "deleting",
    "failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "created",
        "creating",
        "deleted",
        "deleting",
        "failed",
    )
)


def serialize_json(value: EndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> EndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointStatus value: {data!r}")
    return cast(EndpointStatus, data)
