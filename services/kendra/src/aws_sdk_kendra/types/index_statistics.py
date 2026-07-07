"""Generated from Smithy shape ``com.amazonaws.kendra#IndexStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.faq_statistics
    import aws_sdk_kendra.types.text_document_statistics


class IndexStatistics(TypedDict, closed=True):
    faq_statistics: "aws_sdk_kendra.types.faq_statistics.FaqStatistics"
    """<p>The number of question and answer topics in the index.</p>"""
    text_document_statistics: (
        "aws_sdk_kendra.types.text_document_statistics.TextDocumentStatistics"
    )
    """<p>The number of text documents indexed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexStatistics) -> dict:
    out: dict = {}
    import aws_sdk_kendra.types.faq_statistics

    out["FaqStatistics"] = aws_sdk_kendra.types.faq_statistics.serialize_aws_json_1_1(
        value["faq_statistics"]
    )
    import aws_sdk_kendra.types.text_document_statistics

    out["TextDocumentStatistics"] = (
        aws_sdk_kendra.types.text_document_statistics.serialize_aws_json_1_1(
            value["text_document_statistics"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IndexStatistics:
    out: IndexStatistics = {}  # type: ignore[typeddict-item]
    if "FaqStatistics" in data:
        import aws_sdk_kendra.types.faq_statistics

        out["faq_statistics"] = (
            aws_sdk_kendra.types.faq_statistics.deserialize_aws_json_1_1(
                data["FaqStatistics"]
            )
        )
    else:
        raise DeserializationError("IndexStatistics.faq_statistics required")
    if "TextDocumentStatistics" in data:
        import aws_sdk_kendra.types.text_document_statistics

        out["text_document_statistics"] = (
            aws_sdk_kendra.types.text_document_statistics.deserialize_aws_json_1_1(
                data["TextDocumentStatistics"]
            )
        )
    else:
        raise DeserializationError("IndexStatistics.text_document_statistics required")
    return out
