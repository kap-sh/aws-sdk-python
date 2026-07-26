"""Generated from Smithy shape ``com.amazonaws.codestarconnections#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_connections.types.subnet_id

SubnetIds: TypeAlias = list["capo_codestar_connections.types.subnet_id.SubnetId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubnetIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SubnetIds:
    return list(data)
