"""Generated from Smithy shape ``com.amazonaws.glue#StatisticEvaluationLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

StatisticEvaluationLevel: TypeAlias = Literal[
    "Dataset",
    "Column",
    "Multicolumn",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Dataset",
        "Column",
        "Multicolumn",
    )
)


def serialize_aws_json_1_1(value: StatisticEvaluationLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatisticEvaluationLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatisticEvaluationLevel value: {data!r}")
    return cast(StatisticEvaluationLevel, data)
