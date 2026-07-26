"""Generated from Smithy shape ``com.amazonaws.apprunner#ServiceStatus``."""

from typing import Literal, TypeAlias, cast

ServiceStatus: TypeAlias = Literal[
    "CREATE_FAILED",
    "RUNNING",
    "DELETED",
    "DELETE_FAILED",
    "PAUSED",
    "OPERATION_IN_PROGRESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ServiceStatus:
    return cast(ServiceStatus, data)
