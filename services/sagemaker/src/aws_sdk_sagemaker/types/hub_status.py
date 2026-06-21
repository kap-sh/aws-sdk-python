"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubStatus``."""

from typing import Literal, TypeAlias, cast

HubStatus: TypeAlias = Literal[
    "InService",
    "Creating",
    "Updating",
    "Deleting",
    "CreateFailed",
    "UpdateFailed",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubStatus:
    return cast(HubStatus, data)
