"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ResourceIdList``."""

from typing import TypeAlias

ResourceIdList: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ResourceIdList:
    return list(data)
