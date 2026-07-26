"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentStandardOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.document_output_format
    import capo_bedrock_data_automation.types.document_standard_extraction
    import capo_bedrock_data_automation.types.document_standard_generative_field


class DocumentStandardOutputConfiguration(TypedDict, closed=True):
    extraction: NotRequired[
        "capo_bedrock_data_automation.types.document_standard_extraction.DocumentStandardExtraction"
    ]
    generative_field: NotRequired[
        "capo_bedrock_data_automation.types.document_standard_generative_field.DocumentStandardGenerativeField"
    ]
    output_format: NotRequired[
        "capo_bedrock_data_automation.types.document_output_format.DocumentOutputFormat"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentStandardOutputConfiguration) -> dict:
    out: dict = {}
    if "extraction" in value:
        import capo_bedrock_data_automation.types.document_standard_extraction

        out["extraction"] = (
            capo_bedrock_data_automation.types.document_standard_extraction.serialize_json(
                value["extraction"]
            )
        )
    if "generative_field" in value:
        import capo_bedrock_data_automation.types.document_standard_generative_field

        out["generativeField"] = (
            capo_bedrock_data_automation.types.document_standard_generative_field.serialize_json(
                value["generative_field"]
            )
        )
    if "output_format" in value:
        import capo_bedrock_data_automation.types.document_output_format

        out["outputFormat"] = (
            capo_bedrock_data_automation.types.document_output_format.serialize_json(
                value["output_format"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentStandardOutputConfiguration:
    out: DocumentStandardOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "extraction" in data:
        import capo_bedrock_data_automation.types.document_standard_extraction

        out["extraction"] = (
            capo_bedrock_data_automation.types.document_standard_extraction.deserialize_json(
                data["extraction"]
            )
        )
    if "generativeField" in data:
        import capo_bedrock_data_automation.types.document_standard_generative_field

        out["generative_field"] = (
            capo_bedrock_data_automation.types.document_standard_generative_field.deserialize_json(
                data["generativeField"]
            )
        )
    if "outputFormat" in data:
        import capo_bedrock_data_automation.types.document_output_format

        out["output_format"] = (
            capo_bedrock_data_automation.types.document_output_format.deserialize_json(
                data["outputFormat"]
            )
        )
    return out
