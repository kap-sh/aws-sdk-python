"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckImpossibleFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_logic_warning
    import aws_sdk_bedrock.types.automated_reasoning_check_rule_list
    import aws_sdk_bedrock.types.automated_reasoning_check_translation


class AutomatedReasoningCheckImpossibleFinding(TypedDict, closed=True):
    translation: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_translation.AutomatedReasoningCheckTranslation"
    ]
    """<p>The logical translation of the input that this finding evaluates.</p>"""
    contradicting_rules: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_rule_list.AutomatedReasoningCheckRuleList"
    ]
    """<p>The automated reasoning policy rules that contradict the claims and/or premises in the input.</p>"""
    logic_warning: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_logic_warning.AutomatedReasoningCheckLogicWarning"
    ]
    """<p>Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckImpossibleFinding) -> dict:
    out: dict = {}
    if "translation" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_translation

        out["translation"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_translation.serialize_json(
                value["translation"]
            )
        )
    if "contradicting_rules" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_rule_list

        out["contradictingRules"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_rule_list.serialize_json(
                value["contradicting_rules"]
            )
        )
    if "logic_warning" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_logic_warning

        out["logicWarning"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_logic_warning.serialize_json(
                value["logic_warning"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckImpossibleFinding:
    out: AutomatedReasoningCheckImpossibleFinding = {}  # type: ignore[typeddict-item]
    if "translation" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_translation

        out["translation"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_translation.deserialize_json(
                data["translation"]
            )
        )
    if "contradictingRules" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_rule_list

        out["contradicting_rules"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_rule_list.deserialize_json(
                data["contradictingRules"]
            )
        )
    if "logicWarning" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_logic_warning

        out["logic_warning"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_logic_warning.deserialize_json(
                data["logicWarning"]
            )
        )
    return out
