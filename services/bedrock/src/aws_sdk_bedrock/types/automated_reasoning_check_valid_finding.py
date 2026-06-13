"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckValidFinding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_logic_warning
    import aws_sdk_bedrock.types.automated_reasoning_check_rule_list
    import aws_sdk_bedrock.types.automated_reasoning_check_scenario
    import aws_sdk_bedrock.types.automated_reasoning_check_translation


class AutomatedReasoningCheckValidFinding(TypedDict):
    translation: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_translation.AutomatedReasoningCheckTranslation"
    ]
    """<p>The logical translation of the input that this finding validates.</p>"""
    claims_true_scenario: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_scenario.AutomatedReasoningCheckScenario"
    ]
    """<p>An example scenario demonstrating how the claims are logically true.</p>"""
    supporting_rules: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_rule_list.AutomatedReasoningCheckRuleList"
    ]
    """<p>The automated reasoning policy rules that support why this result is considered valid.</p>"""
    logic_warning: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_logic_warning.AutomatedReasoningCheckLogicWarning"
    ]
    """<p>Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckValidFinding) -> dict:
    out: dict = {}
    if "translation" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_translation

        out["translation"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_translation.serialize_json(
                value["translation"]
            )
        )
    if "claims_true_scenario" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_scenario

        out["claimsTrueScenario"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_scenario.serialize_json(
                value["claims_true_scenario"]
            )
        )
    if "supporting_rules" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_rule_list

        out["supportingRules"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_rule_list.serialize_json(
                value["supporting_rules"]
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


def deserialize_json(data: dict) -> AutomatedReasoningCheckValidFinding:
    out: AutomatedReasoningCheckValidFinding = {}  # type: ignore[typeddict-item]
    if "translation" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_translation

        out["translation"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_translation.deserialize_json(
                data["translation"]
            )
        )
    if "claimsTrueScenario" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_scenario

        out["claims_true_scenario"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_scenario.deserialize_json(
                data["claimsTrueScenario"]
            )
        )
    if "supportingRules" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_rule_list

        out["supporting_rules"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_rule_list.deserialize_json(
                data["supportingRules"]
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
