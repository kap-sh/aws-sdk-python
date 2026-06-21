"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnalysisType``."""

from typing import Literal, TypeAlias, cast

AnalysisType: TypeAlias = Literal[
    "MAX_SAVINGS",
    "CUSTOM_COMMITMENT",
    "TARGET_AVERAGE_COVERAGE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnalysisType:
    return cast(AnalysisType, data)
