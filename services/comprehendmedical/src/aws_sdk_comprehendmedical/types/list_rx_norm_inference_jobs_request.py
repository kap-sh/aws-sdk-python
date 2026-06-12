"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ListRxNormInferenceJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter
    import aws_sdk_comprehendmedical.types.max_results_integer
    import aws_sdk_comprehendmedical.types.string


class ListRxNormInferenceJobsRequest(TypedDict):
    filter: NotRequired[
        "aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter.ComprehendMedicalAsyncJobFilter"
    ]
    """<p>Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.</p>"""
    next_token: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""
    max_results: NotRequired[
        "aws_sdk_comprehendmedical.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRxNormInferenceJobsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter

        out["Filter"] = (
            aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRxNormInferenceJobsRequest:
    out: ListRxNormInferenceJobsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter

        out["filter"] = (
            aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
