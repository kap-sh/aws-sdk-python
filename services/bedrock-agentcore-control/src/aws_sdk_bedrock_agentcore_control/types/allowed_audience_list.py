"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AllowedAudienceList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.allowed_audience

AllowedAudienceList: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.allowed_audience.AllowedAudience"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedAudienceList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedAudienceList:
    return list(data)