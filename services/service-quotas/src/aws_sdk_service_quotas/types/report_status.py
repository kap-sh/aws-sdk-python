"""Generated from Smithy shape ``com.amazonaws.servicequotas#ReportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

ReportStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ReportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportStatus value: {data!r}")
    return cast(ReportStatus, data)
