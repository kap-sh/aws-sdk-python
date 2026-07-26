"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnalysisStatus``."""

from typing import Literal, TypeAlias, cast

AnalysisStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "PROCESSING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnalysisStatus:
    return cast(AnalysisStatus, data)
