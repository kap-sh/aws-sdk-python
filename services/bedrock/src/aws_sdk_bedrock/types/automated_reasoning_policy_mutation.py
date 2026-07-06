"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyMutation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_mutation
    import aws_sdk_bedrock.types.automated_reasoning_policy_add_type_mutation
    import aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_mutation
    import aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_mutation
    import aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_mutation
    import aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_mutation
    import aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_mutation
    import aws_sdk_bedrock.types.automated_reasoning_policy_update_type_mutation
    import aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_mutation


class _AutomatedReasoningPolicyMutation_addType(TypedDict, closed=True):
    addType: "aws_sdk_bedrock.types.automated_reasoning_policy_add_type_mutation.AutomatedReasoningPolicyAddTypeMutation"


class _AutomatedReasoningPolicyMutation_updateType(TypedDict, closed=True):
    updateType: "aws_sdk_bedrock.types.automated_reasoning_policy_update_type_mutation.AutomatedReasoningPolicyUpdateTypeMutation"


class _AutomatedReasoningPolicyMutation_deleteType(TypedDict, closed=True):
    deleteType: "aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_mutation.AutomatedReasoningPolicyDeleteTypeMutation"


class _AutomatedReasoningPolicyMutation_addVariable(TypedDict, closed=True):
    addVariable: "aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_mutation.AutomatedReasoningPolicyAddVariableMutation"


class _AutomatedReasoningPolicyMutation_updateVariable(TypedDict, closed=True):
    updateVariable: "aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_mutation.AutomatedReasoningPolicyUpdateVariableMutation"


class _AutomatedReasoningPolicyMutation_deleteVariable(TypedDict, closed=True):
    deleteVariable: "aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_mutation.AutomatedReasoningPolicyDeleteVariableMutation"


class _AutomatedReasoningPolicyMutation_addRule(TypedDict, closed=True):
    addRule: "aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_mutation.AutomatedReasoningPolicyAddRuleMutation"


class _AutomatedReasoningPolicyMutation_updateRule(TypedDict, closed=True):
    updateRule: "aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_mutation.AutomatedReasoningPolicyUpdateRuleMutation"


class _AutomatedReasoningPolicyMutation_deleteRule(TypedDict, closed=True):
    deleteRule: "aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_mutation.AutomatedReasoningPolicyDeleteRuleMutation"


AutomatedReasoningPolicyMutation: TypeAlias = (
    _AutomatedReasoningPolicyMutation_addType
    | _AutomatedReasoningPolicyMutation_updateType
    | _AutomatedReasoningPolicyMutation_deleteType
    | _AutomatedReasoningPolicyMutation_addVariable
    | _AutomatedReasoningPolicyMutation_updateVariable
    | _AutomatedReasoningPolicyMutation_deleteVariable
    | _AutomatedReasoningPolicyMutation_addRule
    | _AutomatedReasoningPolicyMutation_updateRule
    | _AutomatedReasoningPolicyMutation_deleteRule
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyMutation) -> dict:
    if "addType" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_type_mutation

        return {
            "addType": aws_sdk_bedrock.types.automated_reasoning_policy_add_type_mutation.serialize_json(
                value["addType"]
            )
        }
    elif "updateType" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_type_mutation

        return {
            "updateType": aws_sdk_bedrock.types.automated_reasoning_policy_update_type_mutation.serialize_json(
                value["updateType"]
            )
        }
    elif "deleteType" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_mutation

        return {
            "deleteType": aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_mutation.serialize_json(
                value["deleteType"]
            )
        }
    elif "addVariable" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_mutation

        return {
            "addVariable": aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_mutation.serialize_json(
                value["addVariable"]
            )
        }
    elif "updateVariable" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_mutation

        return {
            "updateVariable": aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_mutation.serialize_json(
                value["updateVariable"]
            )
        }
    elif "deleteVariable" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_mutation

        return {
            "deleteVariable": aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_mutation.serialize_json(
                value["deleteVariable"]
            )
        }
    elif "addRule" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_mutation

        return {
            "addRule": aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_mutation.serialize_json(
                value["addRule"]
            )
        }
    elif "updateRule" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_mutation

        return {
            "updateRule": aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_mutation.serialize_json(
                value["updateRule"]
            )
        }
    elif "deleteRule" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_mutation

        return {
            "deleteRule": aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_mutation.serialize_json(
                value["deleteRule"]
            )
        }
    else:
        raise SerializationError("AutomatedReasoningPolicyMutation: no variant present")


def deserialize_json(data: dict) -> AutomatedReasoningPolicyMutation:
    if "addType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_type_mutation

        return {
            "addType": aws_sdk_bedrock.types.automated_reasoning_policy_add_type_mutation.deserialize_json(
                data["addType"]
            )
        }
    elif "updateType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_type_mutation

        return {
            "updateType": aws_sdk_bedrock.types.automated_reasoning_policy_update_type_mutation.deserialize_json(
                data["updateType"]
            )
        }
    elif "deleteType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_mutation

        return {
            "deleteType": aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_mutation.deserialize_json(
                data["deleteType"]
            )
        }
    elif "addVariable" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_mutation

        return {
            "addVariable": aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_mutation.deserialize_json(
                data["addVariable"]
            )
        }
    elif "updateVariable" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_mutation

        return {
            "updateVariable": aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_mutation.deserialize_json(
                data["updateVariable"]
            )
        }
    elif "deleteVariable" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_mutation

        return {
            "deleteVariable": aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_mutation.deserialize_json(
                data["deleteVariable"]
            )
        }
    elif "addRule" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_mutation

        return {
            "addRule": aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_mutation.deserialize_json(
                data["addRule"]
            )
        }
    elif "updateRule" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_mutation

        return {
            "updateRule": aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_mutation.deserialize_json(
                data["updateRule"]
            )
        }
    elif "deleteRule" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_mutation

        return {
            "deleteRule": aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_mutation.deserialize_json(
                data["deleteRule"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyMutation: no recognized variant key"
        )
