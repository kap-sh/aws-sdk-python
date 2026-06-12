"""Generated from Smithy shape ``com.amazonaws.ssm#SignalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

SignalType: TypeAlias = Literal[
    "Approve",
    "Reject",
    "StartStep",
    "StopStep",
    "Resume",
    "Revoke",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Approve",
        "Reject",
        "StartStep",
        "StopStep",
        "Resume",
        "Revoke",
    )
)


def serialize_aws_json_1_1(value: SignalType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SignalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SignalType value: {data!r}")
    return cast(SignalType, data)
