"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StringList``."""

from typing import TypeAlias

StringList: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StringList:
    return list(data)
