"""Generated from Smithy shape ``com.amazonaws.apprunner#ServiceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

ServiceStatus: TypeAlias = Literal[
    "CREATE_FAILED",
    "RUNNING",
    "DELETED",
    "DELETE_FAILED",
    "PAUSED",
    "OPERATION_IN_PROGRESS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_FAILED",
        "RUNNING",
        "DELETED",
        "DELETE_FAILED",
        "PAUSED",
        "OPERATION_IN_PROGRESS",
    )
)


def serialize_aws_json_1_0(value: ServiceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ServiceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceStatus value: {data!r}")
    return cast(ServiceStatus, data)
