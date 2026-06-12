"""Generated from Smithy shape ``com.amazonaws.sagemaker#SoftwareUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SoftwareUpdateStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Succeeded",
    "Failed",
    "RollbackInProgress",
    "RollbackComplete",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Succeeded",
        "Failed",
        "RollbackInProgress",
        "RollbackComplete",
    )
)


def serialize_aws_json_1_1(value: SoftwareUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SoftwareUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SoftwareUpdateStatus value: {data!r}")
    return cast(SoftwareUpdateStatus, data)
