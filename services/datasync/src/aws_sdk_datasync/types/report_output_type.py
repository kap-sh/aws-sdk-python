"""Generated from Smithy shape ``com.amazonaws.datasync#ReportOutputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

ReportOutputType: TypeAlias = Literal[
    "SUMMARY_ONLY",
    "STANDARD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUMMARY_ONLY",
        "STANDARD",
    )
)


def serialize_aws_json_1_1(value: ReportOutputType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportOutputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportOutputType value: {data!r}")
    return cast(ReportOutputType, data)
