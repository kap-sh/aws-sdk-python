"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

EndpointStatus: TypeAlias = Literal[
    "OutOfService",
    "Creating",
    "Updating",
    "SystemUpdating",
    "RollingBack",
    "InService",
    "Deleting",
    "Failed",
    "UpdateRollbackFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OutOfService",
        "Creating",
        "Updating",
        "SystemUpdating",
        "RollingBack",
        "InService",
        "Deleting",
        "Failed",
        "UpdateRollbackFailed",
    )
)


def serialize_aws_json_1_1(value: EndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointStatus value: {data!r}")
    return cast(EndpointStatus, data)
