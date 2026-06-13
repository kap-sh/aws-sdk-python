"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionElement``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable


class _AutomatedReasoningPolicyDefinitionElement_policyDefinitionVariable(TypedDict):
    policyDefinitionVariable: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable.AutomatedReasoningPolicyDefinitionVariable"


class _AutomatedReasoningPolicyDefinitionElement_policyDefinitionType(TypedDict):
    policyDefinitionType: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.AutomatedReasoningPolicyDefinitionType"


class _AutomatedReasoningPolicyDefinitionElement_policyDefinitionRule(TypedDict):
    policyDefinitionRule: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.AutomatedReasoningPolicyDefinitionRule"


AutomatedReasoningPolicyDefinitionElement: TypeAlias = (
    _AutomatedReasoningPolicyDefinitionElement_policyDefinitionVariable
    | _AutomatedReasoningPolicyDefinitionElement_policyDefinitionType
    | _AutomatedReasoningPolicyDefinitionElement_policyDefinitionRule
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionElement) -> dict:
    if "policyDefinitionVariable" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable

        return {
            "policyDefinitionVariable": aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable.serialize_json(
                value["policyDefinitionVariable"]
            )
        }
    elif "policyDefinitionType" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type

        return {
            "policyDefinitionType": aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.serialize_json(
                value["policyDefinitionType"]
            )
        }
    elif "policyDefinitionRule" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule

        return {
            "policyDefinitionRule": aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.serialize_json(
                value["policyDefinitionRule"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyDefinitionElement: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionElement:
    if "policyDefinitionVariable" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable

        return {
            "policyDefinitionVariable": aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable.deserialize_json(
                data["policyDefinitionVariable"]
            )
        }
    elif "policyDefinitionType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type

        return {
            "policyDefinitionType": aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.deserialize_json(
                data["policyDefinitionType"]
            )
        }
    elif "policyDefinitionRule" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule

        return {
            "policyDefinitionRule": aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.deserialize_json(
                data["policyDefinitionRule"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionElement: no recognized variant key"
        )
