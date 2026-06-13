"""Generated from Smithy shape ``com.amazonaws.qbusiness#OrchestrationControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

OrchestrationControl: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: OrchestrationControl) -> str:
    return value


def deserialize_json(data: str) -> OrchestrationControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrchestrationControl value: {data!r}")
    return cast(OrchestrationControl, data)
