"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppStatus``."""

from typing import Literal, TypeAlias, cast

PartnerAppStatus: TypeAlias = Literal[
    "Creating",
    "Updating",
    "Deleting",
    "Available",
    "Failed",
    "UpdateFailed",
    "Deleted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerAppStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartnerAppStatus:
    return cast(PartnerAppStatus, data)
