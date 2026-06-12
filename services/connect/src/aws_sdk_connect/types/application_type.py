"""Generated from Smithy shape ``com.amazonaws.connect#ApplicationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ApplicationType: TypeAlias = Literal[
    "MCP",
    "THIRD_PARTY_APPLICATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MCP",
        "THIRD_PARTY_APPLICATION",
    )
)


def serialize_json(value: ApplicationType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationType value: {data!r}")
    return cast(ApplicationType, data)
