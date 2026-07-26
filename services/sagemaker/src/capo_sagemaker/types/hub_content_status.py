"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentStatus``."""

from typing import Literal, TypeAlias, cast

HubContentStatus: TypeAlias = Literal[
    "Available",
    "Importing",
    "Deleting",
    "ImportFailed",
    "DeleteFailed",
    "PendingImport",
    "PendingDelete",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubContentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubContentStatus:
    return cast(HubContentStatus, data)
