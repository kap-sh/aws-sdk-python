"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

StateMachineStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
    )
)


def serialize_aws_json_1_0(value: StateMachineStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StateMachineStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StateMachineStatus value: {data!r}")
    return cast(StateMachineStatus, data)
