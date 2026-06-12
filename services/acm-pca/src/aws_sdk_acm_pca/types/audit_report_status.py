"""Generated from Smithy shape ``com.amazonaws.acmpca#AuditReportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

AuditReportStatus: TypeAlias = Literal[
    "CREATING",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "SUCCESS",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: AuditReportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuditReportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuditReportStatus value: {data!r}")
    return cast(AuditReportStatus, data)
