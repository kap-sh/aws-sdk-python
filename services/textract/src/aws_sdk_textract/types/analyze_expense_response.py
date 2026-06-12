"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeExpenseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.document_metadata
    import aws_sdk_textract.types.expense_document_list


class AnalyzeExpenseResponse(TypedDict):
    document_metadata: NotRequired[
        "aws_sdk_textract.types.document_metadata.DocumentMetadata"
    ]
    expense_documents: NotRequired[
        "aws_sdk_textract.types.expense_document_list.ExpenseDocumentList"
    ]
    """<p>The expenses detected by Amazon Textract.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeExpenseResponse) -> dict:
    out: dict = {}
    if "document_metadata" in value:
        import aws_sdk_textract.types.document_metadata

        out["DocumentMetadata"] = (
            aws_sdk_textract.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "expense_documents" in value:
        import aws_sdk_textract.types.expense_document_list

        out["ExpenseDocuments"] = (
            aws_sdk_textract.types.expense_document_list.serialize_aws_json_1_1(
                value["expense_documents"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyzeExpenseResponse:
    out: AnalyzeExpenseResponse = {}  # type: ignore[typeddict-item]
    if "DocumentMetadata" in data:
        import aws_sdk_textract.types.document_metadata

        out["document_metadata"] = (
            aws_sdk_textract.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if "ExpenseDocuments" in data:
        import aws_sdk_textract.types.expense_document_list

        out["expense_documents"] = (
            aws_sdk_textract.types.expense_document_list.deserialize_aws_json_1_1(
                data["ExpenseDocuments"]
            )
        )
    return out
