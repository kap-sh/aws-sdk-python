"""Generated from Smithy shape ``com.amazonaws.sagemaker#DomainStatus``."""

from typing import Literal, TypeAlias, cast

DomainStatus: TypeAlias = Literal[
    "Deleting",
    "Failed",
    "InService",
    "Pending",
    "Updating",
    "Update_Failed",
    "Delete_Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainStatus:
    return cast(DomainStatus, data)
