"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListLabelingJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.labeling_job_summary_list
    import capo_sagemaker.types.next_token


class ListLabelingJobsResponse(TypedDict, closed=True):
    labeling_job_summary_list: NotRequired[
        "capo_sagemaker.types.labeling_job_summary_list.LabelingJobSummaryList"
    ]
    """<p>An array of <code>LabelingJobSummary</code> objects, each describing a labeling job.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of labeling jobs, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLabelingJobsResponse) -> dict:
    out: dict = {}
    if "labeling_job_summary_list" in value:
        import capo_sagemaker.types.labeling_job_summary_list

        out["LabelingJobSummaryList"] = (
            capo_sagemaker.types.labeling_job_summary_list.serialize_aws_json_1_1(
                value["labeling_job_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLabelingJobsResponse:
    out: ListLabelingJobsResponse = {}  # type: ignore[typeddict-item]
    if "LabelingJobSummaryList" in data:
        import capo_sagemaker.types.labeling_job_summary_list

        out["labeling_job_summary_list"] = (
            capo_sagemaker.types.labeling_job_summary_list.deserialize_aws_json_1_1(
                data["LabelingJobSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
