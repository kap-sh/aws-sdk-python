"""Generated from Smithy shape ``com.amazonaws.codeconnections#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.subnet_id

SubnetIds: TypeAlias = list["aws_sdk_codeconnections.types.subnet_id.SubnetId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubnetIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SubnetIds:
    return list(data)
