"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#VpcIds``."""

from typing import TypeAlias

VpcIds: TypeAlias = list["str"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VpcIds:
    return list(data)
