"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckTranslationAmbiguousFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_difference_scenario_list
    import aws_sdk_bedrock.types.automated_reasoning_check_translation_option_list


class AutomatedReasoningCheckTranslationAmbiguousFinding(TypedDict, closed=True):
    options: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_translation_option_list.AutomatedReasoningCheckTranslationOptionList"
    ]
    """<p>Different logical interpretations that were detected during translation of the input.</p>"""
    difference_scenarios: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_difference_scenario_list.AutomatedReasoningCheckDifferenceScenarioList"
    ]
    """<p>Scenarios showing how the different translation options differ in meaning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckTranslationAmbiguousFinding) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_translation_option_list

        out["options"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_translation_option_list.serialize_json(
                value["options"]
            )
        )
    if "difference_scenarios" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_difference_scenario_list

        out["differenceScenarios"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_difference_scenario_list.serialize_json(
                value["difference_scenarios"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckTranslationAmbiguousFinding:
    out: AutomatedReasoningCheckTranslationAmbiguousFinding = {}  # type: ignore[typeddict-item]
    if "options" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_translation_option_list

        out["options"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_translation_option_list.deserialize_json(
                data["options"]
            )
        )
    if "differenceScenarios" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_difference_scenario_list

        out["difference_scenarios"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_difference_scenario_list.deserialize_json(
                data["differenceScenarios"]
            )
        )
    return out
