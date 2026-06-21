"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateCampaignAction``."""

from typing import Literal, TypeAlias, cast

UpdateCampaignAction: TypeAlias = Literal[
    "APPROVE",
    "SUSPEND",
    "RESUME",
    "UPDATE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCampaignAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> UpdateCampaignAction:
    return cast(UpdateCampaignAction, data)
