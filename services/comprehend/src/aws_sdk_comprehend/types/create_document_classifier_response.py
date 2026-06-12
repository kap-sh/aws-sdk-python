"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateDocumentClassifierResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classifier_arn


class CreateDocumentClassifierResponse(TypedDict):
    document_classifier_arn: NotRequired[
        "aws_sdk_comprehend.types.document_classifier_arn.DocumentClassifierArn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the document classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDocumentClassifierResponse) -> dict:
    out: dict = {}
    if "document_classifier_arn" in value:
        out["DocumentClassifierArn"] = value["document_classifier_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDocumentClassifierResponse:
    out: CreateDocumentClassifierResponse = {}  # type: ignore[typeddict-item]
    if "DocumentClassifierArn" in data:
        out["document_classifier_arn"] = data["DocumentClassifierArn"]
    return out
