"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomClaimValidationsType``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.custom_claim_validation_type

CustomClaimValidationsType: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.custom_claim_validation_type.CustomClaimValidationType"]


# --- restJson1 ser/de ---
def serialize_json(value: CustomClaimValidationsType) -> list:
    import aws_sdk_bedrock_agentcore_control.types.custom_claim_validation_type
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore_control.types.custom_claim_validation_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomClaimValidationsType:
    import aws_sdk_bedrock_agentcore_control.types.custom_claim_validation_type
    out: CustomClaimValidationsType = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore_control.types.custom_claim_validation_type.deserialize_json(item))
    return out