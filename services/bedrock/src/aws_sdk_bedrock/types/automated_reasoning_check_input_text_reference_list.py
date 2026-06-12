"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckInputTextReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference

AutomatedReasoningCheckInputTextReferenceList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference.AutomatedReasoningCheckInputTextReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckInputTextReferenceList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningCheckInputTextReferenceList:
    import aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference

    out: AutomatedReasoningCheckInputTextReferenceList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference.deserialize_json(
                item
            )
        )
    return out
