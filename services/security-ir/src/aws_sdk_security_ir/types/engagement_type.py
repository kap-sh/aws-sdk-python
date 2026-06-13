"""Generated from Smithy shape ``com.amazonaws.securityir#EngagementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

EngagementType: TypeAlias = Literal[
    "Security Incident",
    "Investigation",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Security Incident",
        "Investigation",
    )
)


def serialize_json(value: EngagementType) -> str:
    return value


def deserialize_json(data: str) -> EngagementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EngagementType value: {data!r}")
    return cast(EngagementType, data)
