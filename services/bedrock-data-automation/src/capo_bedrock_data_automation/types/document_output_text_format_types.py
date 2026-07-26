"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentOutputTextFormatTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.document_output_text_format_type

DocumentOutputTextFormatTypes: TypeAlias = list[
    "capo_bedrock_data_automation.types.document_output_text_format_type.DocumentOutputTextFormatType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentOutputTextFormatTypes) -> list:
    import capo_bedrock_data_automation.types.document_output_text_format_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.document_output_text_format_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DocumentOutputTextFormatTypes:
    import capo_bedrock_data_automation.types.document_output_text_format_type

    out: DocumentOutputTextFormatTypes = []
    for item in data:
        out.append(
            capo_bedrock_data_automation.types.document_output_text_format_type.deserialize_json(
                item
            )
        )
    return out
