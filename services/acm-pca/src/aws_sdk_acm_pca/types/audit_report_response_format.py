"""Generated from Smithy shape ``com.amazonaws.acmpca#AuditReportResponseFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

AuditReportResponseFormat: TypeAlias = Literal[
    "JSON",
    "CSV",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "CSV",
    )
)


def serialize_aws_json_1_1(value: AuditReportResponseFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuditReportResponseFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuditReportResponseFormat value: {data!r}")
    return cast(AuditReportResponseFormat, data)
