"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunStateReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_synthetics.errors import DeserializationError

CanaryRunStateReasonCode: TypeAlias = Literal[
    "CANARY_FAILURE",
    "EXECUTION_FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CANARY_FAILURE",
        "EXECUTION_FAILURE",
    )
)


def serialize_json(value: CanaryRunStateReasonCode) -> str:
    return value


def deserialize_json(data: str) -> CanaryRunStateReasonCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CanaryRunStateReasonCode value: {data!r}")
    return cast(CanaryRunStateReasonCode, data)
