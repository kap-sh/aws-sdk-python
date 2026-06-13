"""Generated from Smithy shape ``com.amazonaws.bedrock#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

Status: TypeAlias = Literal[
    "REGISTERED",
    "INCOMPATIBLE_ENDPOINT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGISTERED",
        "INCOMPATIBLE_ENDPOINT",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
