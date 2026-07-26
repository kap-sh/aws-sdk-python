"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListJobSchemaVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.job_category
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token


class ListJobSchemaVersionsRequest(TypedDict, closed=True):
    job_category: NotRequired["capo_sagemaker.types.job_category.JobCategory"]
    """<p>The category of job schemas to list.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, this token retrieves the next set of results.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of schema versions to return in the response. The default value is 5.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListJobSchemaVersionsRequest) -> dict:
    out: dict = {}
    if "job_category" in value:
        import capo_sagemaker.types.job_category

        out["JobCategory"] = capo_sagemaker.types.job_category.serialize_aws_json_1_1(
            value["job_category"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListJobSchemaVersionsRequest:
    out: ListJobSchemaVersionsRequest = {}  # type: ignore[typeddict-item]
    if "JobCategory" in data:
        import capo_sagemaker.types.job_category

        out["job_category"] = (
            capo_sagemaker.types.job_category.deserialize_aws_json_1_1(
                data["JobCategory"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
