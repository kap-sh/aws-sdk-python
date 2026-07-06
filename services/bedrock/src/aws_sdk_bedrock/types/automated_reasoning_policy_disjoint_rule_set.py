"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDisjointRuleSet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list


class AutomatedReasoningPolicyDisjointRuleSet(TypedDict, closed=True):
    variables: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list.AutomatedReasoningPolicyDefinitionVariableNameList"
    """<p>The set of variables that are used by the rules in this disjoint set.</p>"""
    rules: "aws_sdk_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list.AutomatedReasoningPolicyDisjointedRuleIdList"
    """<p>The list of rules that form this disjoint set, all operating on the same set of variables.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDisjointRuleSet) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list

    out["variables"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list.serialize_json(
            value["variables"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list

    out["rules"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list.serialize_json(
            value["rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDisjointRuleSet:
    out: AutomatedReasoningPolicyDisjointRuleSet = {}  # type: ignore[typeddict-item]
    if "variables" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list

        out["variables"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list.deserialize_json(
                data["variables"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDisjointRuleSet.variables required"
        )
    if "rules" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list

        out["rules"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_disjointed_rule_id_list.deserialize_json(
                data["rules"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDisjointRuleSet.rules required"
        )
    return out
