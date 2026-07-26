"""Generated from Smithy shape ``com.amazonaws.b2bi#CodeList``."""

from typing import TypeAlias

CodeList: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CodeList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> CodeList:
    return list(data)
