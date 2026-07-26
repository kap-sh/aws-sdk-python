"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "OPPORTUNITY",
    "BENEFIT_ALLOCATION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    return cast(ResourceType, data)
