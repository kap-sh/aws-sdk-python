"""Generated from Smithy shape ``com.amazonaws.quicksight#InlineCustomInstruction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.inline_custom_instruction_text
    import aws_sdk_quicksight.types.uploaded_document_metadata


class InlineCustomInstruction(TypedDict):
    instruction_text: "aws_sdk_quicksight.types.inline_custom_instruction_text.InlineCustomInstructionText"
    """<p>The instruction text content.</p>"""
    uploaded_document_metadata: NotRequired[
        "aws_sdk_quicksight.types.uploaded_document_metadata.UploadedDocumentMetadata"
    ]
    """<p>Metadata about an uploaded document associated with this instruction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineCustomInstruction) -> dict:
    out: dict = {}
    out["InstructionText"] = value["instruction_text"]
    if "uploaded_document_metadata" in value:
        import aws_sdk_quicksight.types.uploaded_document_metadata

        out["UploadedDocumentMetadata"] = (
            aws_sdk_quicksight.types.uploaded_document_metadata.serialize_json(
                value["uploaded_document_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> InlineCustomInstruction:
    out: InlineCustomInstruction = {}  # type: ignore[typeddict-item]
    if "InstructionText" in data:
        out["instruction_text"] = data["InstructionText"]
    else:
        raise DeserializationError("InlineCustomInstruction.instruction_text required")
    if "UploadedDocumentMetadata" in data:
        import aws_sdk_quicksight.types.uploaded_document_metadata

        out["uploaded_document_metadata"] = (
            aws_sdk_quicksight.types.uploaded_document_metadata.deserialize_json(
                data["UploadedDocumentMetadata"]
            )
        )
    return out
