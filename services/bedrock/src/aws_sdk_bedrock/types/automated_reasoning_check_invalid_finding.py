"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckInvalidFinding``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_logic_warning
    import aws_sdk_bedrock.types.automated_reasoning_check_rule_list
    import aws_sdk_bedrock.types.automated_reasoning_check_translation


class AutomatedReasoningCheckInvalidFinding(TypedDict):
    translation: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_translation.AutomatedReasoningCheckTranslation"
    ]
    """<p>The logical translation of the input that this finding invalidates.</p>"""
    contradicting_rules: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_rule_list.AutomatedReasoningCheckRuleList"
    ]
    """<p>The automated reasoning policy rules that contradict the claims in the input.</p>"""
    logic_warning: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_logic_warning.AutomatedReasoningCheckLogicWarning"
    ]
    """<p>Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckInvalidFinding) -> dict:
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


def deserialize_json(data: dict) -> AutomatedReasoningCheckInvalidFinding:
    out: AutomatedReasoningCheckInvalidFinding = {}  # type: ignore[typeddict-item]
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
