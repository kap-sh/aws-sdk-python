"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

ExportStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
    "IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "SUCCEEDED",
        "IN_PROGRESS",
    )
)


def serialize_aws_json_1_1(value: ExportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportStatus value: {data!r}")
    return cast(ExportStatus, data)
