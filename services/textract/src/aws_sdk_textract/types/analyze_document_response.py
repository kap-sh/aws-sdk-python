"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeDocumentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.block_list
    import aws_sdk_textract.types.document_metadata
    import aws_sdk_textract.types.human_loop_activation_output
    import aws_sdk_textract.types.string


class AnalyzeDocumentResponse(TypedDict, closed=True):
    document_metadata: NotRequired[
        "aws_sdk_textract.types.document_metadata.DocumentMetadata"
    ]
    """<p>Metadata about the analyzed document. An example is the number of pages.</p>"""
    blocks: NotRequired["aws_sdk_textract.types.block_list.BlockList"]
    """<p>The items that are detected and analyzed by <code>AnalyzeDocument</code>.</p>"""
    human_loop_activation_output: NotRequired[
        "aws_sdk_textract.types.human_loop_activation_output.HumanLoopActivationOutput"
    ]
    """<p>Shows the results of the human in the loop evaluation.</p>"""
    analyze_document_model_version: NotRequired["aws_sdk_textract.types.string.String"]
    """<p>The version of the model used to analyze the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeDocumentResponse) -> dict:
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
    if "human_loop_activation_output" in value:
        import aws_sdk_textract.types.human_loop_activation_output

        out["HumanLoopActivationOutput"] = (
            aws_sdk_textract.types.human_loop_activation_output.serialize_aws_json_1_1(
                value["human_loop_activation_output"]
            )
        )
    if "analyze_document_model_version" in value:
        out["AnalyzeDocumentModelVersion"] = value["analyze_document_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyzeDocumentResponse:
    out: AnalyzeDocumentResponse = {}  # type: ignore[typeddict-item]
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
    if "HumanLoopActivationOutput" in data:
        import aws_sdk_textract.types.human_loop_activation_output

        out["human_loop_activation_output"] = (
            aws_sdk_textract.types.human_loop_activation_output.deserialize_aws_json_1_1(
                data["HumanLoopActivationOutput"]
            )
        )
    if "AnalyzeDocumentModelVersion" in data:
        out["analyze_document_model_version"] = data["AnalyzeDocumentModelVersion"]
    return out
