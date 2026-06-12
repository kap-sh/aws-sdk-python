"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeIDRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.document_pages


class AnalyzeIDRequest(TypedDict):
    document_pages: "aws_sdk_textract.types.document_pages.DocumentPages"
    """<p>The document being passed to AnalyzeID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeIDRequest) -> dict:
    out: dict = {}
    import aws_sdk_textract.types.document_pages

    out["DocumentPages"] = aws_sdk_textract.types.document_pages.serialize_aws_json_1_1(
        value["document_pages"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyzeIDRequest:
    out: AnalyzeIDRequest = {}  # type: ignore[typeddict-item]
    if "DocumentPages" in data:
        import aws_sdk_textract.types.document_pages

        out["document_pages"] = (
            aws_sdk_textract.types.document_pages.deserialize_aws_json_1_1(
                data["DocumentPages"]
            )
        )
    else:
        raise DeserializationError("AnalyzeIDRequest.document_pages required")
    return out
