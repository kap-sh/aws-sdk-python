"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#EvaluationFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

EvaluationFrequency: TypeAlias = Literal[
    "ONE_MIN",
    "FIVE_MIN",
    "TEN_MIN",
    "FIFTEEN_MIN",
    "THIRTY_MIN",
    "ONE_HOUR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_MIN",
        "FIVE_MIN",
        "TEN_MIN",
        "FIFTEEN_MIN",
        "THIRTY_MIN",
        "ONE_HOUR",
    )
)


def serialize_aws_json_1_1(value: EvaluationFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EvaluationFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationFrequency value: {data!r}")
    return cast(EvaluationFrequency, data)
