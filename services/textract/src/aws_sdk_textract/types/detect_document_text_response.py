"""Generated from Smithy shape ``com.amazonaws.textract#DetectDocumentTextResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.block_list
    import aws_sdk_textract.types.document_metadata
    import aws_sdk_textract.types.string


class DetectDocumentTextResponse(TypedDict):
    document_metadata: NotRequired[
        "aws_sdk_textract.types.document_metadata.DocumentMetadata"
    ]
    """<p>Metadata about the document. It contains the number of pages that are detected in the document.</p>"""
    blocks: NotRequired["aws_sdk_textract.types.block_list.BlockList"]
    """<p>An array of <code>Block</code> objects that contain the text that's detected in the document.</p>"""
    detect_document_text_model_version: NotRequired[
        "aws_sdk_textract.types.string.String"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectDocumentTextResponse) -> dict:
    out: dict = {}
    if "document_metadata" in value:
        import aws_sdk_textract.types.document_metadata

        out["DocumentMetadata"] = (
            aws_sdk_textract.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "blocks" in value:
        import aws_sdk_textract.types.block_list

        out["Blocks"] = aws_sdk_textract.types.block_list.serialize_aws_json_1_1(
            value["blocks"]
        )
    if "detect_document_text_model_version" in value:
        out["DetectDocumentTextModelVersion"] = value[
            "detect_document_text_model_version"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectDocumentTextResponse:
    out: DetectDocumentTextResponse = {}  # type: ignore[typeddict-item]
    if "DocumentMetadata" in data:
        import aws_sdk_textract.types.document_metadata

        out["document_metadata"] = (
            aws_sdk_textract.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if "Blocks" in data:
        import aws_sdk_textract.types.block_list

        out["blocks"] = aws_sdk_textract.types.block_list.deserialize_aws_json_1_1(
            data["Blocks"]
        )
    if "DetectDocumentTextModelVersion" in data:
        out["detect_document_text_model_version"] = data[
            "DetectDocumentTextModelVersion"
        ]
    return out
