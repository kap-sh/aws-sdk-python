"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Subnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.subnet_id

Subnets: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.subnet_id.SubnetId"]


# --- restJson1 ser/de ---
def serialize_json(value: Subnets) -> list:
    return list(value)


def deserialize_json(data: list) -> Subnets:
    return list(data)
