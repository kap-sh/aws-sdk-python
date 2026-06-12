"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnalysisStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

AnalysisStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "PROCESSING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "PROCESSING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: AnalysisStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnalysisStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisStatus value: {data!r}")
    return cast(AnalysisStatus, data)
