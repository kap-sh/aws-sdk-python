"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceValueType``."""

from typing import Literal, TypeAlias, cast

ResourceValueType: TypeAlias = Literal["RESOURCE_ID",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceValueType:
    return cast(ResourceValueType, data)
