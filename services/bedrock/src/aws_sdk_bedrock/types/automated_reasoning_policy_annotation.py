"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotation``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_add_type_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_ingest_content_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_update_type_annotation
    import aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_annotation


class _AutomatedReasoningPolicyAnnotation_addType(TypedDict):
    addType: "aws_sdk_bedrock.types.automated_reasoning_policy_add_type_annotation.AutomatedReasoningPolicyAddTypeAnnotation"


class _AutomatedReasoningPolicyAnnotation_updateType(TypedDict):
    updateType: "aws_sdk_bedrock.types.automated_reasoning_policy_update_type_annotation.AutomatedReasoningPolicyUpdateTypeAnnotation"


class _AutomatedReasoningPolicyAnnotation_deleteType(TypedDict):
    deleteType: "aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_annotation.AutomatedReasoningPolicyDeleteTypeAnnotation"


class _AutomatedReasoningPolicyAnnotation_addVariable(TypedDict):
    addVariable: "aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_annotation.AutomatedReasoningPolicyAddVariableAnnotation"


class _AutomatedReasoningPolicyAnnotation_updateVariable(TypedDict):
    updateVariable: "aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_annotation.AutomatedReasoningPolicyUpdateVariableAnnotation"


class _AutomatedReasoningPolicyAnnotation_deleteVariable(TypedDict):
    deleteVariable: "aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_annotation.AutomatedReasoningPolicyDeleteVariableAnnotation"


class _AutomatedReasoningPolicyAnnotation_addRule(TypedDict):
    addRule: "aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_annotation.AutomatedReasoningPolicyAddRuleAnnotation"


class _AutomatedReasoningPolicyAnnotation_updateRule(TypedDict):
    updateRule: "aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_annotation.AutomatedReasoningPolicyUpdateRuleAnnotation"


class _AutomatedReasoningPolicyAnnotation_deleteRule(TypedDict):
    deleteRule: "aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_annotation.AutomatedReasoningPolicyDeleteRuleAnnotation"


class _AutomatedReasoningPolicyAnnotation_addRuleFromNaturalLanguage(TypedDict):
    addRuleFromNaturalLanguage: "aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation.AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation"


class _AutomatedReasoningPolicyAnnotation_updateFromRulesFeedback(TypedDict):
    updateFromRulesFeedback: "aws_sdk_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation.AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation"


class _AutomatedReasoningPolicyAnnotation_updateFromScenarioFeedback(TypedDict):
    updateFromScenarioFeedback: "aws_sdk_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation.AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation"


class _AutomatedReasoningPolicyAnnotation_ingestContent(TypedDict):
    ingestContent: "aws_sdk_bedrock.types.automated_reasoning_policy_ingest_content_annotation.AutomatedReasoningPolicyIngestContentAnnotation"


AutomatedReasoningPolicyAnnotation: TypeAlias = (
    _AutomatedReasoningPolicyAnnotation_addType
    | _AutomatedReasoningPolicyAnnotation_updateType
    | _AutomatedReasoningPolicyAnnotation_deleteType
    | _AutomatedReasoningPolicyAnnotation_addVariable
    | _AutomatedReasoningPolicyAnnotation_updateVariable
    | _AutomatedReasoningPolicyAnnotation_deleteVariable
    | _AutomatedReasoningPolicyAnnotation_addRule
    | _AutomatedReasoningPolicyAnnotation_updateRule
    | _AutomatedReasoningPolicyAnnotation_deleteRule
    | _AutomatedReasoningPolicyAnnotation_addRuleFromNaturalLanguage
    | _AutomatedReasoningPolicyAnnotation_updateFromRulesFeedback
    | _AutomatedReasoningPolicyAnnotation_updateFromScenarioFeedback
    | _AutomatedReasoningPolicyAnnotation_ingestContent
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotation) -> dict:
    if "addType" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_type_annotation

        return {
            "addType": aws_sdk_bedrock.types.automated_reasoning_policy_add_type_annotation.serialize_json(
                value["addType"]
            )
        }
    elif "updateType" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_type_annotation

        return {
            "updateType": aws_sdk_bedrock.types.automated_reasoning_policy_update_type_annotation.serialize_json(
                value["updateType"]
            )
        }
    elif "deleteType" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_annotation

        return {
            "deleteType": aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_annotation.serialize_json(
                value["deleteType"]
            )
        }
    elif "addVariable" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_annotation

        return {
            "addVariable": aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_annotation.serialize_json(
                value["addVariable"]
            )
        }
    elif "updateVariable" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_annotation

        return {
            "updateVariable": aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_annotation.serialize_json(
                value["updateVariable"]
            )
        }
    elif "deleteVariable" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_annotation

        return {
            "deleteVariable": aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_annotation.serialize_json(
                value["deleteVariable"]
            )
        }
    elif "addRule" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_annotation

        return {
            "addRule": aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_annotation.serialize_json(
                value["addRule"]
            )
        }
    elif "updateRule" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_annotation

        return {
            "updateRule": aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_annotation.serialize_json(
                value["updateRule"]
            )
        }
    elif "deleteRule" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_annotation

        return {
            "deleteRule": aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_annotation.serialize_json(
                value["deleteRule"]
            )
        }
    elif "addRuleFromNaturalLanguage" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation

        return {
            "addRuleFromNaturalLanguage": aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation.serialize_json(
                value["addRuleFromNaturalLanguage"]
            )
        }
    elif "updateFromRulesFeedback" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation

        return {
            "updateFromRulesFeedback": aws_sdk_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation.serialize_json(
                value["updateFromRulesFeedback"]
            )
        }
    elif "updateFromScenarioFeedback" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation

        return {
            "updateFromScenarioFeedback": aws_sdk_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation.serialize_json(
                value["updateFromScenarioFeedback"]
            )
        }
    elif "ingestContent" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_ingest_content_annotation

        return {
            "ingestContent": aws_sdk_bedrock.types.automated_reasoning_policy_ingest_content_annotation.serialize_json(
                value["ingestContent"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyAnnotation: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAnnotation:
    if "addType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_type_annotation

        return {
            "addType": aws_sdk_bedrock.types.automated_reasoning_policy_add_type_annotation.deserialize_json(
                data["addType"]
            )
        }
    elif "updateType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_type_annotation

        return {
            "updateType": aws_sdk_bedrock.types.automated_reasoning_policy_update_type_annotation.deserialize_json(
                data["updateType"]
            )
        }
    elif "deleteType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_annotation

        return {
            "deleteType": aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_annotation.deserialize_json(
                data["deleteType"]
            )
        }
    elif "addVariable" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_annotation

        return {
            "addVariable": aws_sdk_bedrock.types.automated_reasoning_policy_add_variable_annotation.deserialize_json(
                data["addVariable"]
            )
        }
    elif "updateVariable" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_annotation

        return {
            "updateVariable": aws_sdk_bedrock.types.automated_reasoning_policy_update_variable_annotation.deserialize_json(
                data["updateVariable"]
            )
        }
    elif "deleteVariable" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_annotation

        return {
            "deleteVariable": aws_sdk_bedrock.types.automated_reasoning_policy_delete_variable_annotation.deserialize_json(
                data["deleteVariable"]
            )
        }
    elif "addRule" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_annotation

        return {
            "addRule": aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_annotation.deserialize_json(
                data["addRule"]
            )
        }
    elif "updateRule" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_annotation

        return {
            "updateRule": aws_sdk_bedrock.types.automated_reasoning_policy_update_rule_annotation.deserialize_json(
                data["updateRule"]
            )
        }
    elif "deleteRule" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_annotation

        return {
            "deleteRule": aws_sdk_bedrock.types.automated_reasoning_policy_delete_rule_annotation.deserialize_json(
                data["deleteRule"]
            )
        }
    elif "addRuleFromNaturalLanguage" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation

        return {
            "addRuleFromNaturalLanguage": aws_sdk_bedrock.types.automated_reasoning_policy_add_rule_from_natural_language_annotation.deserialize_json(
                data["addRuleFromNaturalLanguage"]
            )
        }
    elif "updateFromRulesFeedback" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation

        return {
            "updateFromRulesFeedback": aws_sdk_bedrock.types.automated_reasoning_policy_update_from_rule_feedback_annotation.deserialize_json(
                data["updateFromRulesFeedback"]
            )
        }
    elif "updateFromScenarioFeedback" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation

        return {
            "updateFromScenarioFeedback": aws_sdk_bedrock.types.automated_reasoning_policy_update_from_scenario_feedback_annotation.deserialize_json(
                data["updateFromScenarioFeedback"]
            )
        }
    elif "ingestContent" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_ingest_content_annotation

        return {
            "ingestContent": aws_sdk_bedrock.types.automated_reasoning_policy_ingest_content_annotation.deserialize_json(
                data["ingestContent"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAnnotation: no recognized variant key"
        )
