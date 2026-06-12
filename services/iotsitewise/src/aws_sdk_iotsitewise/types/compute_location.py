"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeLocation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ComputeLocation: TypeAlias = Literal[
    "EDGE",
    "CLOUD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EDGE",
        "CLOUD",
    )
)


def serialize_json(value: ComputeLocation) -> str:
    return value


def deserialize_json(data: str) -> ComputeLocation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeLocation value: {data!r}")
    return cast(ComputeLocation, data)
