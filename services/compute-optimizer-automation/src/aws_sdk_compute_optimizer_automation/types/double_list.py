"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#DoubleList``."""

from typing import TypeAlias

DoubleList: TypeAlias = list["float"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DoubleList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> DoubleList:
    return list(data)
