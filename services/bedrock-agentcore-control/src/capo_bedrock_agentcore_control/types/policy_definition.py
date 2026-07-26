"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.cedar_policy
    import capo_bedrock_agentcore_control.types.policy_generation_details


class _PolicyDefinition_cedar(TypedDict, closed=True):
    cedar: "capo_bedrock_agentcore_control.types.cedar_policy.CedarPolicy"


class _PolicyDefinition_policyGeneration(TypedDict, closed=True):
    policyGeneration: "capo_bedrock_agentcore_control.types.policy_generation_details.PolicyGenerationDetails"


PolicyDefinition: TypeAlias = (
    _PolicyDefinition_cedar | _PolicyDefinition_policyGeneration
)


# --- restJson1 ser/de ---
def serialize_json(value: PolicyDefinition) -> dict:
    if "cedar" in value:
        import capo_bedrock_agentcore_control.types.cedar_policy

        return {
            "cedar": capo_bedrock_agentcore_control.types.cedar_policy.serialize_json(
                value["cedar"]
            )
        }
    elif "policyGeneration" in value:
        import capo_bedrock_agentcore_control.types.policy_generation_details

        return {
            "policyGeneration": capo_bedrock_agentcore_control.types.policy_generation_details.serialize_json(
                value["policyGeneration"]
            )
        }
    else:
        raise SerializationError("PolicyDefinition: no variant present")


def deserialize_json(data: dict) -> PolicyDefinition:
    if "cedar" in data:
        import capo_bedrock_agentcore_control.types.cedar_policy

        return {
            "cedar": capo_bedrock_agentcore_control.types.cedar_policy.deserialize_json(
                data["cedar"]
            )
        }
    elif "policyGeneration" in data:
        import capo_bedrock_agentcore_control.types.policy_generation_details

        return {
            "policyGeneration": capo_bedrock_agentcore_control.types.policy_generation_details.deserialize_json(
                data["policyGeneration"]
            )
        }
    else:
        raise DeserializationError("PolicyDefinition: no recognized variant key")
