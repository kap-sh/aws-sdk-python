"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyScenario``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_result
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_scenario_alternate_expression
    import aws_sdk_bedrock.types.automated_reasoning_policy_scenario_expression


class AutomatedReasoningPolicyScenario(TypedDict):
    expression: "aws_sdk_bedrock.types.automated_reasoning_policy_scenario_expression.AutomatedReasoningPolicyScenarioExpression"
    """<p>The logical expression or condition that defines this test scenario.</p>"""
    alternate_expression: "aws_sdk_bedrock.types.automated_reasoning_policy_scenario_alternate_expression.AutomatedReasoningPolicyScenarioAlternateExpression"
    """<p>An alternative way to express the same test scenario, used for validation and comparison purposes.</p>"""
    expected_result: "aws_sdk_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult"
    """<p>The expected outcome when this scenario is evaluated against the policy (e.g., PASS, FAIL, VIOLATION).</p>"""
    rule_ids: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list.AutomatedReasoningPolicyDefinitionRuleIdList"
    """<p>The list of rule identifiers that are expected to be triggered or evaluated by this test scenario.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyScenario) -> dict:
    out: dict = {}
    out["expression"] = value["expression"]
    out["alternateExpression"] = value["alternate_expression"]
    import aws_sdk_bedrock.types.automated_reasoning_check_result

    out["expectedResult"] = (
        aws_sdk_bedrock.types.automated_reasoning_check_result.serialize_json(
            value["expected_result"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list

    out["ruleIds"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list.serialize_json(
            value["rule_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyScenario:
    out: AutomatedReasoningPolicyScenario = {}  # type: ignore[typeddict-item]
    if "expression" in data:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyScenario.expression required"
        )
    if "alternateExpression" in data:
        out["alternate_expression"] = data["alternateExpression"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyScenario.alternate_expression required"
        )
    if "expectedResult" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_result

        out["expected_result"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_result.deserialize_json(
                data["expectedResult"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyScenario.expected_result required"
        )
    if "ruleIds" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list

        out["rule_ids"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id_list.deserialize_json(
                data["ruleIds"]
            )
        )
    else:
        raise DeserializationError("AutomatedReasoningPolicyScenario.rule_ids required")
    return out
