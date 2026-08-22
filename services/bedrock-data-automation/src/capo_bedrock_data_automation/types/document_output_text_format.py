"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentOutputTextFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.document_output_text_format_types


class DocumentOutputTextFormat(TypedDict, closed=True):
    types: NotRequired[
        "capo_bedrock_data_automation.types.document_output_text_format_types.DocumentOutputTextFormatTypes"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentOutputTextFormat) -> dict:
    out: dict = {}
    if "types" in value:
        import capo_bedrock_data_automation.types.document_output_text_format_types

        out["types"] = (
            capo_bedrock_data_automation.types.document_output_text_format_types.serialize_json(
                value["types"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentOutputTextFormat:
    out: DocumentOutputTextFormat = {}  # type: ignore[typeddict-item]
    if data.get("types") is not None:
        import capo_bedrock_data_automation.types.document_output_text_format_types

        out["types"] = (
            capo_bedrock_data_automation.types.document_output_text_format_types.deserialize_json(
                data["types"]
            )
        )
    return out
