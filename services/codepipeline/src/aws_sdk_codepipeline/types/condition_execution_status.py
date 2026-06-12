"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

ConditionExecutionStatus: TypeAlias = Literal[
    "InProgress",
    "Failed",
    "Errored",
    "Succeeded",
    "Cancelled",
    "Abandoned",
    "Overridden",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Failed",
        "Errored",
        "Succeeded",
        "Cancelled",
        "Abandoned",
        "Overridden",
    )
)


def serialize_aws_json_1_1(value: ConditionExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConditionExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConditionExecutionStatus value: {data!r}")
    return cast(ConditionExecutionStatus, data)
