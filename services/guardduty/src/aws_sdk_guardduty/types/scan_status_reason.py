"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

ScanStatusReason: TypeAlias = Literal[
    "ACCESS_DENIED",
    "RESOURCE_NOT_FOUND",
    "SNAPSHOT_SIZE_LIMIT_EXCEEDED",
    "RESOURCE_UNAVAILABLE",
    "INCONSISTENT_SOURCE",
    "INCREMENTAL_NO_DIFFERENCE",
    "NO_EBS_VOLUMES_FOUND",
    "UNSUPPORTED_PRODUCT_CODE_TYPE",
    "AMI_SNAPSHOT_LIMIT_EXCEEDED",
    "UNRELATED_RESOURCES",
    "BASE_RESOURCE_NOT_SCANNED",
    "BASE_CREATED_AFTER_TARGET",
    "UNSUPPORTED_FOR_INCREMENTAL",
    "UNSUPPORTED_AMI",
    "UNSUPPORTED_SNAPSHOT",
    "UNSUPPORTED_COMPOSITE_RECOVERY_POINT",
    "ALL_FILES_SKIPPED_OR_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCESS_DENIED",
        "RESOURCE_NOT_FOUND",
        "SNAPSHOT_SIZE_LIMIT_EXCEEDED",
        "RESOURCE_UNAVAILABLE",
        "INCONSISTENT_SOURCE",
        "INCREMENTAL_NO_DIFFERENCE",
        "NO_EBS_VOLUMES_FOUND",
        "UNSUPPORTED_PRODUCT_CODE_TYPE",
        "AMI_SNAPSHOT_LIMIT_EXCEEDED",
        "UNRELATED_RESOURCES",
        "BASE_RESOURCE_NOT_SCANNED",
        "BASE_CREATED_AFTER_TARGET",
        "UNSUPPORTED_FOR_INCREMENTAL",
        "UNSUPPORTED_AMI",
        "UNSUPPORTED_SNAPSHOT",
        "UNSUPPORTED_COMPOSITE_RECOVERY_POINT",
        "ALL_FILES_SKIPPED_OR_FAILED",
    )
)


def serialize_json(value: ScanStatusReason) -> str:
    return value


def deserialize_json(data: str) -> ScanStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanStatusReason value: {data!r}")
    return cast(ScanStatusReason, data)
