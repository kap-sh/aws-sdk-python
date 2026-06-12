"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckTranslationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_translation

AutomatedReasoningCheckTranslationList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_check_translation.AutomatedReasoningCheckTranslation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckTranslationList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_check_translation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_check_translation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningCheckTranslationList:
    import aws_sdk_bedrock.types.automated_reasoning_check_translation

    out: AutomatedReasoningCheckTranslationList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_check_translation.deserialize_json(
                item
            )
        )
    return out
