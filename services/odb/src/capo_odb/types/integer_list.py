"""Generated from Smithy shape ``com.amazonaws.odb#IntegerList``."""

from typing import TypeAlias

IntegerList: TypeAlias = list["int"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IntegerList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> IntegerList:
    return list(data)
