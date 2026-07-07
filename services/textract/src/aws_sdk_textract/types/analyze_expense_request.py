"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeExpenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.document


class AnalyzeExpenseRequest(TypedDict, closed=True):
    document: "aws_sdk_textract.types.document.Document"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeExpenseRequest) -> dict:
    out: dict = {}
    import aws_sdk_textract.types.document

    out["Document"] = aws_sdk_textract.types.document.serialize_aws_json_1_1(
        value["document"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyzeExpenseRequest:
    out: AnalyzeExpenseRequest = {}  # type: ignore[typeddict-item]
    if "Document" in data:
        import aws_sdk_textract.types.document

        out["document"] = aws_sdk_textract.types.document.deserialize_aws_json_1_1(
            data["Document"]
        )
    else:
        raise DeserializationError("AnalyzeExpenseRequest.document required")
    return out
