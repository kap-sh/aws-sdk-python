"""Generated from Smithy shape ``com.amazonaws.outposts#SupportedHardwareType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

SupportedHardwareType: TypeAlias = Literal[
    "RACK",
    "SERVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RACK",
        "SERVER",
    )
)


def serialize_json(value: SupportedHardwareType) -> str:
    return value


def deserialize_json(data: str) -> SupportedHardwareType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SupportedHardwareType value: {data!r}")
    return cast(SupportedHardwareType, data)
