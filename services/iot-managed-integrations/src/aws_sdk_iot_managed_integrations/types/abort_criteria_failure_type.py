"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AbortCriteriaFailureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

AbortCriteriaFailureType: TypeAlias = Literal[
    "FAILED",
    "REJECTED",
    "TIMED_OUT",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "REJECTED",
        "TIMED_OUT",
        "ALL",
    )
)


def serialize_json(value: AbortCriteriaFailureType) -> str:
    return value


def deserialize_json(data: str) -> AbortCriteriaFailureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AbortCriteriaFailureType value: {data!r}")
    return cast(AbortCriteriaFailureType, data)
