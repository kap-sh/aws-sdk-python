"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckTranslationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_translation_option

AutomatedReasoningCheckTranslationOptionList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_check_translation_option.AutomatedReasoningCheckTranslationOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckTranslationOptionList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_check_translation_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_check_translation_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningCheckTranslationOptionList:
    import aws_sdk_bedrock.types.automated_reasoning_check_translation_option

    out: AutomatedReasoningCheckTranslationOptionList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_check_translation_option.deserialize_json(
                item
            )
        )
    return out
