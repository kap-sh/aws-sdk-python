"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeDocumentClassifierRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classifier_arn


class DescribeDocumentClassifierRequest(TypedDict):
    document_classifier_arn: (
        "aws_sdk_comprehend.types.document_classifier_arn.DocumentClassifierArn"
    )
    """<p>The Amazon Resource Name (ARN) that identifies the document classifier. The <code>CreateDocumentClassifier</code> operation returns this identifier in its response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDocumentClassifierRequest) -> dict:
    out: dict = {}
    out["DocumentClassifierArn"] = value["document_classifier_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDocumentClassifierRequest:
    out: DescribeDocumentClassifierRequest = {}  # type: ignore[typeddict-item]
    if "DocumentClassifierArn" in data:
        out["document_classifier_arn"] = data["DocumentClassifierArn"]
    else:
        raise DeserializationError(
            "DescribeDocumentClassifierRequest.document_classifier_arn required"
        )
    return out
