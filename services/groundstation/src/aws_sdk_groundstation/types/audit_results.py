"""Generated from Smithy shape ``com.amazonaws.groundstation#AuditResults``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

AuditResults: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_json(value: AuditResults) -> str:
    return value


def deserialize_json(data: str) -> AuditResults:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuditResults value: {data!r}")
    return cast(AuditResults, data)
