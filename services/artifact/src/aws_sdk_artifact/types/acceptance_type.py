"""Generated from Smithy shape ``com.amazonaws.artifact#AcceptanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_artifact.errors import DeserializationError

AcceptanceType: TypeAlias = Literal[
    "PASSTHROUGH",
    "EXPLICIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSTHROUGH",
        "EXPLICIT",
    )
)


def serialize_json(value: AcceptanceType) -> str:
    return value


def deserialize_json(data: str) -> AcceptanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceptanceType value: {data!r}")
    return cast(AcceptanceType, data)
