"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrackingServerMaintenanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrackingServerMaintenanceStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: TrackingServerMaintenanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrackingServerMaintenanceStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrackingServerMaintenanceStatus value: {data!r}"
        )
    return cast(TrackingServerMaintenanceStatus, data)
