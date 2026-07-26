"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ResourceArnList``."""

from typing import TypeAlias

ResourceArnList: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceArnList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ResourceArnList:
    return list(data)
