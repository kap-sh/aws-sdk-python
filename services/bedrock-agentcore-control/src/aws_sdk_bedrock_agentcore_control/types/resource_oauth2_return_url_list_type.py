"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ResourceOauth2ReturnUrlListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_type

ResourceOauth2ReturnUrlListType: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_type.ResourceOauth2ReturnUrlType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceOauth2ReturnUrlListType) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceOauth2ReturnUrlListType:
    return list(data)
