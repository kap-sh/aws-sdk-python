"""Generated from Smithy shape ``com.amazonaws.comprehend#ListDocumentClassificationJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classification_job_properties_list
    import aws_sdk_comprehend.types.string


class ListDocumentClassificationJobsResponse(TypedDict):
    document_classification_job_properties_list: NotRequired[
        "aws_sdk_comprehend.types.document_classification_job_properties_list.DocumentClassificationJobPropertiesList"
    ]
    """<p>A list containing the properties of each job returned.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentClassificationJobsResponse) -> dict:
    out: dict = {}
    if "document_classification_job_properties_list" in value:
        import aws_sdk_comprehend.types.document_classification_job_properties_list

        out["DocumentClassificationJobPropertiesList"] = (
            aws_sdk_comprehend.types.document_classification_job_properties_list.serialize_aws_json_1_1(
                value["document_classification_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentClassificationJobsResponse:
    out: ListDocumentClassificationJobsResponse = {}  # type: ignore[typeddict-item]
    if "DocumentClassificationJobPropertiesList" in data:
        import aws_sdk_comprehend.types.document_classification_job_properties_list

        out["document_classification_job_properties_list"] = (
            aws_sdk_comprehend.types.document_classification_job_properties_list.deserialize_aws_json_1_1(
                data["DocumentClassificationJobPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
