"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SubSlotValueElicitationSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.prompt_specification
    import aws_sdk_lex_models_v2.types.sample_utterances_list
    import aws_sdk_lex_models_v2.types.slot_default_value_specification
    import aws_sdk_lex_models_v2.types.wait_and_continue_specification


class SubSlotValueElicitationSetting(TypedDict, closed=True):
    default_value_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_default_value_specification.SlotDefaultValueSpecification"
    ]
    prompt_specification: (
        "aws_sdk_lex_models_v2.types.prompt_specification.PromptSpecification"
    )
    sample_utterances: NotRequired[
        "aws_sdk_lex_models_v2.types.sample_utterances_list.SampleUtterancesList"
    ]
    """<p>If you know a specific pattern that users might respond to an Amazon Lex request for a sub slot value, you can provide those utterances to improve accuracy. This is optional. In most cases Amazon Lex is capable of understanding user utterances. This is similar to <code>SampleUtterances</code> for slots.</p>"""
    wait_and_continue_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.wait_and_continue_specification.WaitAndContinueSpecification"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SubSlotValueElicitationSetting) -> dict:
    out: dict = {}
    if "default_value_specification" in value:
        import aws_sdk_lex_models_v2.types.slot_default_value_specification

        out["defaultValueSpecification"] = (
            aws_sdk_lex_models_v2.types.slot_default_value_specification.serialize_json(
                value["default_value_specification"]
            )
        )
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
    return out


def deserialize_json(data: dict) -> SubSlotValueElicitationSetting:
    out: SubSlotValueElicitationSetting = {}  # type: ignore[typeddict-item]
    if "defaultValueSpecification" in data:
        import aws_sdk_lex_models_v2.types.slot_default_value_specification

        out["default_value_specification"] = (
            aws_sdk_lex_models_v2.types.slot_default_value_specification.deserialize_json(
                data["defaultValueSpecification"]
            )
        )
    if "promptSpecification" in data:
        import aws_sdk_lex_models_v2.types.prompt_specification

        out["prompt_specification"] = (
            aws_sdk_lex_models_v2.types.prompt_specification.deserialize_json(
                data["promptSpecification"]
            )
        )
    else:
        raise DeserializationError(
            "SubSlotValueElicitationSetting.prompt_specification required"
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
    return out
