"""Generated from Smithy shape ``com.amazonaws.textract#Extraction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.expense_document
    import aws_sdk_textract.types.identity_document
    import aws_sdk_textract.types.lending_document


class Extraction(TypedDict, closed=True):
    lending_document: NotRequired[
        "aws_sdk_textract.types.lending_document.LendingDocument"
    ]
    """<p>Holds the structured data returned by AnalyzeDocument for lending documents.</p>"""
    expense_document: NotRequired[
        "aws_sdk_textract.types.expense_document.ExpenseDocument"
    ]
    identity_document: NotRequired[
        "aws_sdk_textract.types.identity_document.IdentityDocument"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Extraction) -> dict:
    out: dict = {}
    if "lending_document" in value:
        import aws_sdk_textract.types.lending_document

        out["LendingDocument"] = (
            aws_sdk_textract.types.lending_document.serialize_aws_json_1_1(
                value["lending_document"]
            )
        )
    if "expense_document" in value:
        import aws_sdk_textract.types.expense_document

        out["ExpenseDocument"] = (
            aws_sdk_textract.types.expense_document.serialize_aws_json_1_1(
                value["expense_document"]
            )
        )
    if "identity_document" in value:
        import aws_sdk_textract.types.identity_document

        out["IdentityDocument"] = (
            aws_sdk_textract.types.identity_document.serialize_aws_json_1_1(
                value["identity_document"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Extraction:
    out: Extraction = {}  # type: ignore[typeddict-item]
    if "LendingDocument" in data:
        import aws_sdk_textract.types.lending_document

        out["lending_document"] = (
            aws_sdk_textract.types.lending_document.deserialize_aws_json_1_1(
                data["LendingDocument"]
            )
        )
    if "ExpenseDocument" in data:
        import aws_sdk_textract.types.expense_document

        out["expense_document"] = (
            aws_sdk_textract.types.expense_document.deserialize_aws_json_1_1(
                data["ExpenseDocument"]
            )
        )
    if "IdentityDocument" in data:
        import aws_sdk_textract.types.identity_document

        out["identity_document"] = (
            aws_sdk_textract.types.identity_document.deserialize_aws_json_1_1(
                data["IdentityDocument"]
            )
        )
    return out
