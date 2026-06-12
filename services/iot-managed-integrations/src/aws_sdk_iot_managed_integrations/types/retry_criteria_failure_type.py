"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RetryCriteriaFailureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

RetryCriteriaFailureType: TypeAlias = Literal[
    "FAILED",
    "TIMED_OUT",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "TIMED_OUT",
        "ALL",
    )
)


def serialize_json(value: RetryCriteriaFailureType) -> str:
    return value


def deserialize_json(data: str) -> RetryCriteriaFailureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetryCriteriaFailureType value: {data!r}")
    return cast(RetryCriteriaFailureType, data)
