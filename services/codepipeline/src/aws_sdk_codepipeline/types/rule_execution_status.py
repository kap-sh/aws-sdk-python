"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

RuleExecutionStatus: TypeAlias = Literal[
    "InProgress",
    "Abandoned",
    "Succeeded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Abandoned",
        "Succeeded",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: RuleExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleExecutionStatus value: {data!r}")
    return cast(RuleExecutionStatus, data)
