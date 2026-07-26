"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CampaignStatus``."""

from typing import Literal, TypeAlias, cast

CampaignStatus: TypeAlias = Literal[
    "CREATING",
    "WAITING_FOR_APPROVAL",
    "RUNNING",
    "SUSPENDED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CampaignStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CampaignStatus:
    return cast(CampaignStatus, data)
