"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ApnPrograms``."""

from typing import TypeAlias

ApnPrograms: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ApnPrograms) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ApnPrograms:
    return list(data)
