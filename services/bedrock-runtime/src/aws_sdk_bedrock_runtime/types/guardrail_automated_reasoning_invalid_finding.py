"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningInvalidFinding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation


class GuardrailAutomatedReasoningInvalidFinding(TypedDict):
    translation: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation.GuardrailAutomatedReasoningTranslation"
    ]
    """<p>The logical translation of the input that this finding invalidates.</p>"""
    contradicting_rules: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list.GuardrailAutomatedReasoningRuleList"
    ]
    """<p>The automated reasoning policy rules that contradict the claims in the input.</p>"""
    logic_warning: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_logic_warning.GuardrailAutomatedReasoningLogicWarning"
    ]
    """<p>Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningInvalidFinding) -> dict:
    out: dict = {}
    if "translation" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation

        out["translation"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation.serialize_json(
                value["translation"]
            )
        )
    if "contradicting_rules" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list

        out["contradictingRules"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list.serialize_json(
                value["contradicting_rules"]
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


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningInvalidFinding:
    out: GuardrailAutomatedReasoningInvalidFinding = {}  # type: ignore[typeddict-item]
    if "translation" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation

        out["translation"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation.deserialize_json(
                data["translation"]
            )
        )
    if "contradictingRules" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list

        out["contradicting_rules"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_rule_list.deserialize_json(
                data["contradictingRules"]
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
