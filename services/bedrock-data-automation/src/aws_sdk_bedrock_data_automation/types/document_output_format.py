"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentOutputFormat``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.document_output_additional_file_format
    import aws_sdk_bedrock_data_automation.types.document_output_text_format


class DocumentOutputFormat(TypedDict):
    text_format: "aws_sdk_bedrock_data_automation.types.document_output_text_format.DocumentOutputTextFormat"
    additional_file_format: "aws_sdk_bedrock_data_automation.types.document_output_additional_file_format.DocumentOutputAdditionalFileFormat"


# --- restJson1 ser/de ---
def serialize_json(value: DocumentOutputFormat) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.document_output_text_format

    out["textFormat"] = (
        aws_sdk_bedrock_data_automation.types.document_output_text_format.serialize_json(
            value["text_format"]
        )
    )
    import aws_sdk_bedrock_data_automation.types.document_output_additional_file_format

    out["additionalFileFormat"] = (
        aws_sdk_bedrock_data_automation.types.document_output_additional_file_format.serialize_json(
            value["additional_file_format"]
        )
    )
    return out


def deserialize_json(data: dict) -> DocumentOutputFormat:
    out: DocumentOutputFormat = {}  # type: ignore[typeddict-item]
    if "textFormat" in data:
        import aws_sdk_bedrock_data_automation.types.document_output_text_format

        out["text_format"] = (
            aws_sdk_bedrock_data_automation.types.document_output_text_format.deserialize_json(
                data["textFormat"]
            )
        )
    else:
        raise DeserializationError("DocumentOutputFormat.text_format required")
    if "additionalFileFormat" in data:
        import aws_sdk_bedrock_data_automation.types.document_output_additional_file_format

        out["additional_file_format"] = (
            aws_sdk_bedrock_data_automation.types.document_output_additional_file_format.deserialize_json(
                data["additionalFileFormat"]
            )
        )
    else:
        raise DeserializationError(
            "DocumentOutputFormat.additional_file_format required"
        )
    return out
