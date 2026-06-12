"""Generated from Smithy shape ``com.amazonaws.inspector#ReportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

ReportStatus: TypeAlias = Literal[
    "WORK_IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WORK_IN_PROGRESS",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_aws_json_1_1(value: ReportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportStatus value: {data!r}")
    return cast(ReportStatus, data)
