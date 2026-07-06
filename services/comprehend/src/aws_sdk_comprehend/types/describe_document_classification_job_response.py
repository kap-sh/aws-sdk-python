"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeDocumentClassificationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classification_job_properties


class DescribeDocumentClassificationJobResponse(TypedDict, closed=True):
    document_classification_job_properties: NotRequired[
        "aws_sdk_comprehend.types.document_classification_job_properties.DocumentClassificationJobProperties"
    ]
    """<p>An object that describes the properties associated with the document classification job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDocumentClassificationJobResponse) -> dict:
    out: dict = {}
    if "document_classification_job_properties" in value:
        import aws_sdk_comprehend.types.document_classification_job_properties

        out["DocumentClassificationJobProperties"] = (
            aws_sdk_comprehend.types.document_classification_job_properties.serialize_aws_json_1_1(
                value["document_classification_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDocumentClassificationJobResponse:
    out: DescribeDocumentClassificationJobResponse = {}  # type: ignore[typeddict-item]
    if "DocumentClassificationJobProperties" in data:
        import aws_sdk_comprehend.types.document_classification_job_properties

        out["document_classification_job_properties"] = (
            aws_sdk_comprehend.types.document_classification_job_properties.deserialize_aws_json_1_1(
                data["DocumentClassificationJobProperties"]
            )
        )
    return out
