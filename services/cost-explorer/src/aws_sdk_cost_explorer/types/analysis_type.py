"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnalysisType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

AnalysisType: TypeAlias = Literal[
    "MAX_SAVINGS",
    "CUSTOM_COMMITMENT",
    "TARGET_AVERAGE_COVERAGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAX_SAVINGS",
        "CUSTOM_COMMITMENT",
        "TARGET_AVERAGE_COVERAGE",
    )
)


def serialize_aws_json_1_1(value: AnalysisType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnalysisType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisType value: {data!r}")
    return cast(AnalysisType, data)
