"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: EndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointStatus:
    return cast(EndpointStatus, data)
