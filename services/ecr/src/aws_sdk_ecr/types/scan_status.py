"""Generated from Smithy shape ``com.amazonaws.ecr#ScanStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ScanStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
    "UNSUPPORTED_IMAGE",
    "ACTIVE",
    "PENDING",
    "SCAN_ELIGIBILITY_EXPIRED",
    "FINDINGS_UNAVAILABLE",
    "LIMIT_EXCEEDED",
    "IMAGE_ARCHIVED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETE",
        "FAILED",
        "UNSUPPORTED_IMAGE",
        "ACTIVE",
        "PENDING",
        "SCAN_ELIGIBILITY_EXPIRED",
        "FINDINGS_UNAVAILABLE",
        "LIMIT_EXCEEDED",
        "IMAGE_ARCHIVED",
    )
)


def serialize_aws_json_1_1(value: ScanStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScanStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanStatus value: {data!r}")
    return cast(ScanStatus, data)
