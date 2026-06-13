"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningValidFinding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation


class GuardrailAutomatedReasoningValidFinding(TypedDict):
    translation: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation.GuardrailAutomatedReasoningTranslation"
    ]
    """<p>The logical translation of the input that this finding validates.</p>"""
    claims_true_scenario: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario.GuardrailAutomatedReasoningScenario"
    ]
    """<p>An example scenario demonstrating how the claims are logically true.</p>"""
    supporting_rules: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list.GuardrailAutomatedReasoningRuleList"
    ]
    """<p>The automated reasoning policy rules that support why this result is considered valid.</p>"""
    logic_warning: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning.GuardrailAutomatedReasoningLogicWarning"
    ]
    """<p>Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningValidFinding) -> dict:
    out: dict = {}
    if "translation" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation

        out["translation"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation.serialize_json(
                value["translation"]
            )
        )
    if "claims_true_scenario" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario

        out["claimsTrueScenario"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario.serialize_json(
                value["claims_true_scenario"]
            )
        )
    if "supporting_rules" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list

        out["supportingRules"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list.serialize_json(
                value["supporting_rules"]
            )
        )
    if "logic_warning" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning

        out["logicWarning"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning.serialize_json(
                value["logic_warning"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningValidFinding:
    out: GuardrailAutomatedReasoningValidFinding = {}  # type: ignore[typeddict-item]
    if "translation" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation

        out["translation"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation.deserialize_json(
                data["translation"]
            )
        )
    if "claimsTrueScenario" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario

        out["claims_true_scenario"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_scenario.deserialize_json(
                data["claimsTrueScenario"]
            )
        )
    if "supportingRules" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list

        out["supporting_rules"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list.deserialize_json(
                data["supportingRules"]
            )
        )
    if "logicWarning" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning

        out["logic_warning"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning.deserialize_json(
                data["logicWarning"]
            )
        )
    return out
