"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceCountGroupKey``."""

from typing import Literal, TypeAlias, cast

ResourceCountGroupKey: TypeAlias = Literal[
    "RESOURCE_TYPE",
    "ACCOUNT_ID",
    "AWS_REGION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCountGroupKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceCountGroupKey:
    return cast(ResourceCountGroupKey, data)
