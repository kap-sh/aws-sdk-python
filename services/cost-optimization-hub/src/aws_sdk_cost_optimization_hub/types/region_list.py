"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#RegionList``."""

from typing import TypeAlias

RegionList: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegionList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RegionList:
    return list(data)
