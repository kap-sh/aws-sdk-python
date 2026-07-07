"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionQualityReport``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_conflicted_rule_id_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set_list


class AutomatedReasoningPolicyDefinitionQualityReport(TypedDict, closed=True):
    type_count: "int"
    """<p>The total number of custom types defined in the policy.</p>"""
    variable_count: "int"
    """<p>The total number of variables defined in the policy.</p>"""
    rule_count: "int"
    """<p>The total number of rules defined in the policy.</p>"""
    unused_types: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name_list.AutomatedReasoningPolicyDefinitionTypeNameList"
    """<p>A list of custom types that are defined but not referenced by any variables or rules, suggesting they may be unnecessary.</p>"""
    unused_type_values: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair_list.AutomatedReasoningPolicyDefinitionTypeValuePairList"
    """<p>A list of type values that are defined but never used in any rules, indicating potential cleanup opportunities.</p>"""
    unused_variables: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list.AutomatedReasoningPolicyDefinitionVariableNameList"
    """<p>A list of variables that are defined but not referenced by any rules, suggesting they may be unnecessary.</p>"""
    conflicting_rules: "aws_sdk_bedrock.types.automated_reasoning_policy_conflicted_rule_id_list.AutomatedReasoningPolicyConflictedRuleIdList"
    """<p>A list of rules that may conflict with each other, potentially leading to inconsistent policy behavior.</p>"""
    disjoint_rule_sets: "aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set_list.AutomatedReasoningPolicyDisjointRuleSetList"
    """<p>Groups of rules that operate on completely separate sets of variables, indicating the policy may be addressing multiple unrelated concerns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionQualityReport) -> dict:
    out: dict = {}
    out["typeCount"] = value["type_count"]
    out["variableCount"] = value["variable_count"]
    out["ruleCount"] = value["rule_count"]
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name_list

    out["unusedTypes"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name_list.serialize_json(
            value["unused_types"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair_list

    out["unusedTypeValues"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair_list.serialize_json(
            value["unused_type_values"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list

    out["unusedVariables"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list.serialize_json(
            value["unused_variables"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_conflicted_rule_id_list

    out["conflictingRules"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_conflicted_rule_id_list.serialize_json(
            value["conflicting_rules"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set_list

    out["disjointRuleSets"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set_list.serialize_json(
            value["disjoint_rule_sets"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionQualityReport:
    out: AutomatedReasoningPolicyDefinitionQualityReport = {}  # type: ignore[typeddict-item]
    if "typeCount" in data:
        out["type_count"] = data["typeCount"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionQualityReport.type_count required"
        )
    if "variableCount" in data:
        out["variable_count"] = data["variableCount"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionQualityReport.variable_count required"
        )
    if "ruleCount" in data:
        out["rule_count"] = data["ruleCount"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionQualityReport.rule_count required"
        )
    if "unusedTypes" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name_list

        out["unused_types"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name_list.deserialize_json(
                data["unusedTypes"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionQualityReport.unused_types required"
        )
    if "unusedTypeValues" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair_list

        out["unused_type_values"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_pair_list.deserialize_json(
                data["unusedTypeValues"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionQualityReport.unused_type_values required"
        )
    if "unusedVariables" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list

        out["unused_variables"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name_list.deserialize_json(
                data["unusedVariables"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionQualityReport.unused_variables required"
        )
    if "conflictingRules" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_conflicted_rule_id_list

        out["conflicting_rules"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_conflicted_rule_id_list.deserialize_json(
                data["conflictingRules"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionQualityReport.conflicting_rules required"
        )
    if "disjointRuleSets" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set_list

        out["disjoint_rule_sets"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set_list.deserialize_json(
                data["disjointRuleSets"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionQualityReport.disjoint_rule_sets required"
        )
    return out
