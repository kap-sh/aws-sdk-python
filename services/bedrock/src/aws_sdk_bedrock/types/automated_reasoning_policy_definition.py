"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_format_version


class AutomatedReasoningPolicyDefinition(TypedDict, closed=True):
    version: "aws_sdk_bedrock.types.automated_reasoning_policy_format_version.AutomatedReasoningPolicyFormatVersion"
    """<p>The version of the policy definition format.</p>"""
    types: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_list.AutomatedReasoningPolicyDefinitionTypeList"
    ]
    """<p>The custom user-defined vairable types used in the policy. Types are enum-based variable types that provide additional context beyond the predefined variable types.</p>"""
    rules: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_list.AutomatedReasoningPolicyDefinitionRuleList"
    ]
    """<p>The formal logic rules extracted from the source document. Rules define the logical constraints that determine whether model responses are valid, invalid, or satisfiable.</p>"""
    variables: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_list.AutomatedReasoningPolicyDefinitionVariableList"
    ]
    """<p>The variables that represent concepts in the policy. Variables can have values assigned when translating natural language into formal logic. Their descriptions are crucial for accurate translation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinition) -> dict:
    out: dict = {}
    out["version"] = value.get("version", "1")
    if "types" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_list

        out["types"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_list.serialize_json(
                value["types"]
            )
        )
    if "rules" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_list

        out["rules"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_list.serialize_json(
                value["rules"]
            )
        )
    if "variables" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_list

        out["variables"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_list.serialize_json(
                value["variables"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinition:
    out: AutomatedReasoningPolicyDefinition = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        out["version"] = "1"
    if "types" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_list

        out["types"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_list.deserialize_json(
                data["types"]
            )
        )
    if "rules" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_list

        out["rules"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_list.deserialize_json(
                data["rules"]
            )
        )
    if "variables" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_list

        out["variables"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_list.deserialize_json(
                data["variables"]
            )
        )
    return out
