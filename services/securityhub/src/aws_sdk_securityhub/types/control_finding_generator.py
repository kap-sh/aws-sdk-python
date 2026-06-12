"""Generated from Smithy shape ``com.amazonaws.securityhub#ControlFindingGenerator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ControlFindingGenerator: TypeAlias = Literal[
    "STANDARD_CONTROL",
    "SECURITY_CONTROL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD_CONTROL",
        "SECURITY_CONTROL",
    )
)


def serialize_json(value: ControlFindingGenerator) -> str:
    return value


def deserialize_json(data: str) -> ControlFindingGenerator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlFindingGenerator value: {data!r}")
    return cast(ControlFindingGenerator, data)
