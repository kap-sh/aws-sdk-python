"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionElement``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule
    import capo_bedrock.types.automated_reasoning_policy_definition_type
    import capo_bedrock.types.automated_reasoning_policy_definition_variable


class _AutomatedReasoningPolicyDefinitionElement_policyDefinitionVariable(
    TypedDict, closed=True
):
    policyDefinitionVariable: "capo_bedrock.types.automated_reasoning_policy_definition_variable.AutomatedReasoningPolicyDefinitionVariable"


class _AutomatedReasoningPolicyDefinitionElement_policyDefinitionType(
    TypedDict, closed=True
):
    policyDefinitionType: "capo_bedrock.types.automated_reasoning_policy_definition_type.AutomatedReasoningPolicyDefinitionType"


class _AutomatedReasoningPolicyDefinitionElement_policyDefinitionRule(
    TypedDict, closed=True
):
    policyDefinitionRule: "capo_bedrock.types.automated_reasoning_policy_definition_rule.AutomatedReasoningPolicyDefinitionRule"


AutomatedReasoningPolicyDefinitionElement: TypeAlias = (
    _AutomatedReasoningPolicyDefinitionElement_policyDefinitionVariable
    | _AutomatedReasoningPolicyDefinitionElement_policyDefinitionType
    | _AutomatedReasoningPolicyDefinitionElement_policyDefinitionRule
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionElement) -> dict:
    if "policyDefinitionVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable

        return {
            "policyDefinitionVariable": capo_bedrock.types.automated_reasoning_policy_definition_variable.serialize_json(
                value["policyDefinitionVariable"]
            )
        }
    elif "policyDefinitionType" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_type

        return {
            "policyDefinitionType": capo_bedrock.types.automated_reasoning_policy_definition_type.serialize_json(
                value["policyDefinitionType"]
            )
        }
    elif "policyDefinitionRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule

        return {
            "policyDefinitionRule": capo_bedrock.types.automated_reasoning_policy_definition_rule.serialize_json(
                value["policyDefinitionRule"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyDefinitionElement: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionElement:
    if "policyDefinitionVariable" in data:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable

        return {
            "policyDefinitionVariable": capo_bedrock.types.automated_reasoning_policy_definition_variable.deserialize_json(
                data["policyDefinitionVariable"]
            )
        }
    elif "policyDefinitionType" in data:
        import capo_bedrock.types.automated_reasoning_policy_definition_type

        return {
            "policyDefinitionType": capo_bedrock.types.automated_reasoning_policy_definition_type.deserialize_json(
                data["policyDefinitionType"]
            )
        }
    elif "policyDefinitionRule" in data:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule

        return {
            "policyDefinitionRule": capo_bedrock.types.automated_reasoning_policy_definition_rule.deserialize_json(
                data["policyDefinitionRule"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionElement: no recognized variant key"
        )
