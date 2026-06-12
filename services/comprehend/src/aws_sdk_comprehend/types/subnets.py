"""Generated from Smithy shape ``com.amazonaws.comprehend#Subnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.subnet_id

Subnets: TypeAlias = list["aws_sdk_comprehend.types.subnet_id.SubnetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subnets) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Subnets:
    return list(data)
