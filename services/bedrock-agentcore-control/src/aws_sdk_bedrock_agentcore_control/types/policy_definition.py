"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyDefinition``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.cedar_policy
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_details


class _PolicyDefinition_cedar(TypedDict):
    cedar: "aws_sdk_bedrock_agentcore_control.types.cedar_policy.CedarPolicy"


class _PolicyDefinition_policyGeneration(TypedDict):
    policyGeneration: "aws_sdk_bedrock_agentcore_control.types.policy_generation_details.PolicyGenerationDetails"


PolicyDefinition: TypeAlias = (
    _PolicyDefinition_cedar | _PolicyDefinition_policyGeneration
)


# --- restJson1 ser/de ---
def serialize_json(value: PolicyDefinition) -> dict:
    if "cedar" in value:
        import aws_sdk_bedrock_agentcore_control.types.cedar_policy

        return {
            "cedar": aws_sdk_bedrock_agentcore_control.types.cedar_policy.serialize_json(
                value["cedar"]
            )
        }
    elif "policyGeneration" in value:
        import aws_sdk_bedrock_agentcore_control.types.policy_generation_details

        return {
            "policyGeneration": aws_sdk_bedrock_agentcore_control.types.policy_generation_details.serialize_json(
                value["policyGeneration"]
            )
        }
    else:
        raise SerializationError("PolicyDefinition: no variant present")


def deserialize_json(data: dict) -> PolicyDefinition:
    if "cedar" in data:
        import aws_sdk_bedrock_agentcore_control.types.cedar_policy

        return {
            "cedar": aws_sdk_bedrock_agentcore_control.types.cedar_policy.deserialize_json(
                data["cedar"]
            )
        }
    elif "policyGeneration" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_generation_details

        return {
            "policyGeneration": aws_sdk_bedrock_agentcore_control.types.policy_generation_details.deserialize_json(
                data["policyGeneration"]
            )
        }
    else:
        raise DeserializationError("PolicyDefinition: no recognized variant key")
