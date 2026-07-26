"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeDocumentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_description


class DescribeDocumentResult(TypedDict, closed=True):
    document: NotRequired["capo_ssm.types.document_description.DocumentDescription"]
    """<p>Information about the SSM document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDocumentResult) -> dict:
    out: dict = {}
    if "document" in value:
        import capo_ssm.types.document_description

        out["Document"] = capo_ssm.types.document_description.serialize_aws_json_1_1(
            value["document"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDocumentResult:
    out: DescribeDocumentResult = {}  # type: ignore[typeddict-item]
    if "Document" in data:
        import capo_ssm.types.document_description

        out["document"] = capo_ssm.types.document_description.deserialize_aws_json_1_1(
            data["Document"]
        )
    return out
