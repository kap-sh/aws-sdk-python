"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListCandidatesForAutoMLJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_name
    import capo_sagemaker.types.auto_ml_max_results_for_trials
    import capo_sagemaker.types.auto_ml_sort_order
    import capo_sagemaker.types.candidate_name
    import capo_sagemaker.types.candidate_sort_by
    import capo_sagemaker.types.candidate_status
    import capo_sagemaker.types.next_token


class ListCandidatesForAutoMLJobRequest(TypedDict, closed=True):
    auto_ml_job_name: NotRequired["capo_sagemaker.types.auto_ml_job_name.AutoMLJobName"]
    """<p>List the candidates created for the job by providing the job's name.</p>"""
    status_equals: NotRequired["capo_sagemaker.types.candidate_status.CandidateStatus"]
    """<p>List the candidates for the job and filter by status.</p>"""
    candidate_name_equals: NotRequired[
        "capo_sagemaker.types.candidate_name.CandidateName"
    ]
    """<p>List the candidates for the job and filter by candidate name.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.auto_ml_sort_order.AutoMLSortOrder"]
    """<p>The sort order for the results. The default is <code>Ascending</code>.</p>"""
    sort_by: NotRequired["capo_sagemaker.types.candidate_sort_by.CandidateSortBy"]
    """<p>The parameter by which to sort the results. The default is <code>Descending</code>.</p>"""
    max_results: NotRequired[
        "capo_sagemaker.types.auto_ml_max_results_for_trials.AutoMLMaxResultsForTrials"
    ]
    """<p>List the job's candidates up to a specified limit.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCandidatesForAutoMLJobRequest) -> dict:
    out: dict = {}
    if "auto_ml_job_name" in value:
        out["AutoMLJobName"] = value["auto_ml_job_name"]
    if "status_equals" in value:
        import capo_sagemaker.types.candidate_status

        out["StatusEquals"] = (
            capo_sagemaker.types.candidate_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "candidate_name_equals" in value:
        out["CandidateNameEquals"] = value["candidate_name_equals"]
    if "sort_order" in value:
        import capo_sagemaker.types.auto_ml_sort_order

        out["SortOrder"] = (
            capo_sagemaker.types.auto_ml_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "sort_by" in value:
        import capo_sagemaker.types.candidate_sort_by

        out["SortBy"] = capo_sagemaker.types.candidate_sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCandidatesForAutoMLJobRequest:
    out: ListCandidatesForAutoMLJobRequest = {}  # type: ignore[typeddict-item]
    if "AutoMLJobName" in data:
        out["auto_ml_job_name"] = data["AutoMLJobName"]
    if "StatusEquals" in data:
        import capo_sagemaker.types.candidate_status

        out["status_equals"] = (
            capo_sagemaker.types.candidate_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "CandidateNameEquals" in data:
        out["candidate_name_equals"] = data["CandidateNameEquals"]
    if "SortOrder" in data:
        import capo_sagemaker.types.auto_ml_sort_order

        out["sort_order"] = (
            capo_sagemaker.types.auto_ml_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "SortBy" in data:
        import capo_sagemaker.types.candidate_sort_by

        out["sort_by"] = (
            capo_sagemaker.types.candidate_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
