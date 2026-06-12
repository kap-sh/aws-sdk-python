"""Generated from Smithy shape ``com.amazonaws.apprunner#CertificateValidationRecordStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

CertificateValidationRecordStatus: TypeAlias = Literal[
    "PENDING_VALIDATION",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_VALIDATION",
        "SUCCESS",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: CertificateValidationRecordStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CertificateValidationRecordStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CertificateValidationRecordStatus value: {data!r}"
        )
    return cast(CertificateValidationRecordStatus, data)
