"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSecurityLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisSecurityLevel: TypeAlias = Literal[
    "LEVEL_1",
    "LEVEL_2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEVEL_1",
        "LEVEL_2",
    )
)


def serialize_json(value: CisSecurityLevel) -> str:
    return value


def deserialize_json(data: str) -> CisSecurityLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisSecurityLevel value: {data!r}")
    return cast(CisSecurityLevel, data)
