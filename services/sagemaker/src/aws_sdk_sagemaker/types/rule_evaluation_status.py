"""Generated from Smithy shape ``com.amazonaws.sagemaker#RuleEvaluationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RuleEvaluationStatus: TypeAlias = Literal[
    "InProgress",
    "NoIssuesFound",
    "IssuesFound",
    "Error",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "NoIssuesFound",
        "IssuesFound",
        "Error",
        "Stopping",
        "Stopped",
    )
)


def serialize_aws_json_1_1(value: RuleEvaluationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleEvaluationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleEvaluationStatus value: {data!r}")
    return cast(RuleEvaluationStatus, data)
