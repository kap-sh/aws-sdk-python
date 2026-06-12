"""Generated from Smithy shape ``com.amazonaws.comprehend#StopTrainingDocumentClassifierRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classifier_arn


class StopTrainingDocumentClassifierRequest(TypedDict):
    document_classifier_arn: (
        "aws_sdk_comprehend.types.document_classifier_arn.DocumentClassifierArn"
    )
    """<p>The Amazon Resource Name (ARN) that identifies the document classifier currently being trained.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTrainingDocumentClassifierRequest) -> dict:
    out: dict = {}
    out["DocumentClassifierArn"] = value["document_classifier_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTrainingDocumentClassifierRequest:
    out: StopTrainingDocumentClassifierRequest = {}  # type: ignore[typeddict-item]
    if "DocumentClassifierArn" in data:
        out["document_classifier_arn"] = data["DocumentClassifierArn"]
    else:
        raise DeserializationError(
            "StopTrainingDocumentClassifierRequest.document_classifier_arn required"
        )
    return out
