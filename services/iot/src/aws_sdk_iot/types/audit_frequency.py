"""Generated from Smithy shape ``com.amazonaws.iot#AuditFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuditFrequency: TypeAlias = Literal[
    "DAILY",
    "WEEKLY",
    "BIWEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAILY",
        "WEEKLY",
        "BIWEEKLY",
        "MONTHLY",
    )
)


def serialize_json(value: AuditFrequency) -> str:
    return value


def deserialize_json(data: str) -> AuditFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuditFrequency value: {data!r}")
    return cast(AuditFrequency, data)
