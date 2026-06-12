"""Generated from Smithy shape ``com.amazonaws.networkmanager#SendViaMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

SendViaMode: TypeAlias = Literal[
    "dual-hop",
    "single-hop",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "dual-hop",
        "single-hop",
    )
)


def serialize_json(value: SendViaMode) -> str:
    return value


def deserialize_json(data: str) -> SendViaMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SendViaMode value: {data!r}")
    return cast(SendViaMode, data)
