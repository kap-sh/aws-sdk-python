"""Generated from Smithy shape ``com.amazonaws.sagemaker#MaintenanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MaintenanceStatus: TypeAlias = Literal[
    "MaintenanceInProgress",
    "MaintenanceComplete",
    "MaintenanceFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MaintenanceInProgress",
        "MaintenanceComplete",
        "MaintenanceFailed",
    )
)


def serialize_aws_json_1_1(value: MaintenanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaintenanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceStatus value: {data!r}")
    return cast(MaintenanceStatus, data)
