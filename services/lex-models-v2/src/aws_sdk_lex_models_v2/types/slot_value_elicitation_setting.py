"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotValueElicitationSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.prompt_specification
    import aws_sdk_lex_models_v2.types.sample_utterances_list
    import aws_sdk_lex_models_v2.types.slot_capture_setting
    import aws_sdk_lex_models_v2.types.slot_constraint
    import aws_sdk_lex_models_v2.types.slot_default_value_specification
    import aws_sdk_lex_models_v2.types.slot_resolution_setting
    import aws_sdk_lex_models_v2.types.wait_and_continue_specification


class SlotValueElicitationSetting(TypedDict):
    default_value_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_default_value_specification.SlotDefaultValueSpecification"
    ]
    """<p>A list of default values for a slot. Default values are used when Amazon Lex hasn't determined a value for a slot. You can specify default values from context variables, session attributes, and defined values.</p>"""
    slot_constraint: "aws_sdk_lex_models_v2.types.slot_constraint.SlotConstraint"
    """<p>Specifies whether the slot is required or optional.</p>"""
    prompt_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.prompt_specification.PromptSpecification"
    ]
    """<p>The prompt that Amazon Lex uses to elicit the slot value from the user.</p>"""
    sample_utterances: NotRequired[
        "aws_sdk_lex_models_v2.types.sample_utterances_list.SampleUtterancesList"
    ]
    """<p>If you know a specific pattern that users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.</p>"""
    wait_and_continue_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.wait_and_continue_specification.WaitAndContinueSpecification"
    ]
    slot_capture_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_capture_setting.SlotCaptureSetting"
    ]
    """<p>Specifies the settings that Amazon Lex uses when a slot value is successfully entered by a user.</p>"""
    slot_resolution_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_resolution_setting.SlotResolutionSetting"
    ]
    """<p>An object containing information about whether assisted slot resolution is turned on for the slot or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotValueElicitationSetting) -> dict:
    out: dict = {}
    if "default_value_specification" in value:
        import aws_sdk_lex_models_v2.types.slot_default_value_specification

        out["defaultValueSpecification"] = (
            aws_sdk_lex_models_v2.types.slot_default_value_specification.serialize_json(
                value["default_value_specification"]
            )
        )
    import aws_sdk_lex_models_v2.types.slot_constraint

    out["slotConstraint"] = aws_sdk_lex_models_v2.types.slot_constraint.serialize_json(
        value["slot_constraint"]
    )
    if "prompt_specification" in value:
        import aws_sdk_lex_models_v2.types.prompt_specification

        out["promptSpecification"] = (
            aws_sdk_lex_models_v2.types.prompt_specification.serialize_json(
                value["prompt_specification"]
            )
        )
    if "sample_utterances" in value:
        import aws_sdk_lex_models_v2.types.sample_utterances_list

        out["sampleUtterances"] = (
            aws_sdk_lex_models_v2.types.sample_utterances_list.serialize_json(
                value["sample_utterances"]
            )
        )
    if "wait_and_continue_specification" in value:
        import aws_sdk_lex_models_v2.types.wait_and_continue_specification

        out["waitAndContinueSpecification"] = (
            aws_sdk_lex_models_v2.types.wait_and_continue_specification.serialize_json(
                value["wait_and_continue_specification"]
            )
        )
    if "slot_capture_setting" in value:
        import aws_sdk_lex_models_v2.types.slot_capture_setting

        out["slotCaptureSetting"] = (
            aws_sdk_lex_models_v2.types.slot_capture_setting.serialize_json(
                value["slot_capture_setting"]
            )
        )
    if "slot_resolution_setting" in value:
        import aws_sdk_lex_models_v2.types.slot_resolution_setting

        out["slotResolutionSetting"] = (
            aws_sdk_lex_models_v2.types.slot_resolution_setting.serialize_json(
                value["slot_resolution_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlotValueElicitationSetting:
    out: SlotValueElicitationSetting = {}  # type: ignore[typeddict-item]
    if "defaultValueSpecification" in data:
        import aws_sdk_lex_models_v2.types.slot_default_value_specification

        out["default_value_specification"] = (
            aws_sdk_lex_models_v2.types.slot_default_value_specification.deserialize_json(
                data["defaultValueSpecification"]
            )
        )
    if "slotConstraint" in data:
        import aws_sdk_lex_models_v2.types.slot_constraint

        out["slot_constraint"] = (
            aws_sdk_lex_models_v2.types.slot_constraint.deserialize_json(
                data["slotConstraint"]
            )
        )
    else:
        raise DeserializationError(
            "SlotValueElicitationSetting.slot_constraint required"
        )
    if "promptSpecification" in data:
        import aws_sdk_lex_models_v2.types.prompt_specification

        out["prompt_specification"] = (
            aws_sdk_lex_models_v2.types.prompt_specification.deserialize_json(
                data["promptSpecification"]
            )
        )
    if "sampleUtterances" in data:
        import aws_sdk_lex_models_v2.types.sample_utterances_list

        out["sample_utterances"] = (
            aws_sdk_lex_models_v2.types.sample_utterances_list.deserialize_json(
                data["sampleUtterances"]
            )
        )
    if "waitAndContinueSpecification" in data:
        import aws_sdk_lex_models_v2.types.wait_and_continue_specification

        out["wait_and_continue_specification"] = (
            aws_sdk_lex_models_v2.types.wait_and_continue_specification.deserialize_json(
                data["waitAndContinueSpecification"]
            )
        )
    if "slotCaptureSetting" in data:
        import aws_sdk_lex_models_v2.types.slot_capture_setting

        out["slot_capture_setting"] = (
            aws_sdk_lex_models_v2.types.slot_capture_setting.deserialize_json(
                data["slotCaptureSetting"]
            )
        )
    if "slotResolutionSetting" in data:
        import aws_sdk_lex_models_v2.types.slot_resolution_setting

        out["slot_resolution_setting"] = (
            aws_sdk_lex_models_v2.types.slot_resolution_setting.deserialize_json(
                data["slotResolutionSetting"]
            )
        )
    return out
