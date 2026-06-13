"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AudiencesListType``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.audience_type

AudiencesListType: TypeAlias = list["aws_sdk_bedrock_agentcore.types.audience_type.AudienceType"]


# --- restJson1 ser/de ---
def serialize_json(value: AudiencesListType) -> list:
    return list(value)


def deserialize_json(data: list) -> AudiencesListType:
    return list(data)