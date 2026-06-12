"""Generated from Smithy shape ``com.amazonaws.pi#AnalysisStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pi.errors import DeserializationError

AnalysisStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: AnalysisStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnalysisStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisStatus value: {data!r}")
    return cast(AnalysisStatus, data)
