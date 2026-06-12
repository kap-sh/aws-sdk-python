"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ContinuousExportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

ContinuousExportStatus: TypeAlias = Literal[
    "START_IN_PROGRESS",
    "START_FAILED",
    "ACTIVE",
    "ERROR",
    "STOP_IN_PROGRESS",
    "STOP_FAILED",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START_IN_PROGRESS",
        "START_FAILED",
        "ACTIVE",
        "ERROR",
        "STOP_IN_PROGRESS",
        "STOP_FAILED",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: ContinuousExportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContinuousExportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContinuousExportStatus value: {data!r}")
    return cast(ContinuousExportStatus, data)
