"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentStandardOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.document_output_format
    import aws_sdk_bedrock_data_automation.types.document_standard_extraction
    import aws_sdk_bedrock_data_automation.types.document_standard_generative_field


class DocumentStandardOutputConfiguration(TypedDict):
    extraction: NotRequired[
        "aws_sdk_bedrock_data_automation.types.document_standard_extraction.DocumentStandardExtraction"
    ]
    generative_field: NotRequired[
        "aws_sdk_bedrock_data_automation.types.document_standard_generative_field.DocumentStandardGenerativeField"
    ]
    output_format: NotRequired[
        "aws_sdk_bedrock_data_automation.types.document_output_format.DocumentOutputFormat"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentStandardOutputConfiguration) -> dict:
    out: dict = {}
    if "extraction" in value:
        import aws_sdk_bedrock_data_automation.types.document_standard_extraction

        out["extraction"] = (
            aws_sdk_bedrock_data_automation.types.document_standard_extraction.serialize_json(
                value["extraction"]
            )
        )
    if "generative_field" in value:
        import aws_sdk_bedrock_data_automation.types.document_standard_generative_field

        out["generativeField"] = (
            aws_sdk_bedrock_data_automation.types.document_standard_generative_field.serialize_json(
                value["generative_field"]
            )
        )
    if "output_format" in value:
        import aws_sdk_bedrock_data_automation.types.document_output_format

        out["outputFormat"] = (
            aws_sdk_bedrock_data_automation.types.document_output_format.serialize_json(
                value["output_format"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentStandardOutputConfiguration:
    out: DocumentStandardOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "extraction" in data:
        import aws_sdk_bedrock_data_automation.types.document_standard_extraction

        out["extraction"] = (
            aws_sdk_bedrock_data_automation.types.document_standard_extraction.deserialize_json(
                data["extraction"]
            )
        )
    if "generativeField" in data:
        import aws_sdk_bedrock_data_automation.types.document_standard_generative_field

        out["generative_field"] = (
            aws_sdk_bedrock_data_automation.types.document_standard_generative_field.deserialize_json(
                data["generativeField"]
            )
        )
    if "outputFormat" in data:
        import aws_sdk_bedrock_data_automation.types.document_output_format

        out["output_format"] = (
            aws_sdk_bedrock_data_automation.types.document_output_format.deserialize_json(
                data["outputFormat"]
            )
        )
    return out
