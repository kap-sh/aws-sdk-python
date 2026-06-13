"""Generated from Smithy shape ``com.amazonaws.odb#WeeksOfMonth``."""

from typing import TypeAlias

WeeksOfMonth: TypeAlias = list["int"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WeeksOfMonth) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> WeeksOfMonth:
    return list(data)
