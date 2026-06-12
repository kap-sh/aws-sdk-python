"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

StateMachineType: TypeAlias = Literal[
    "STANDARD",
    "EXPRESS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "EXPRESS",
    )
)


def serialize_aws_json_1_0(value: StateMachineType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StateMachineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StateMachineType value: {data!r}")
    return cast(StateMachineType, data)
