"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListLabelingJobsForWorkteamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.labeling_job_for_workteam_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListLabelingJobsForWorkteamResponse(TypedDict, closed=True):
    labeling_job_summary_list: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_for_workteam_summary_list.LabelingJobForWorkteamSummaryList"
    ]
    """<p>An array of <code>LabelingJobSummary</code> objects, each describing a labeling job.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of labeling jobs, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLabelingJobsForWorkteamResponse) -> dict:
    out: dict = {}
    if "labeling_job_summary_list" in value:
        import aws_sdk_sagemaker.types.labeling_job_for_workteam_summary_list

        out["LabelingJobSummaryList"] = (
            aws_sdk_sagemaker.types.labeling_job_for_workteam_summary_list.serialize_aws_json_1_1(
                value["labeling_job_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLabelingJobsForWorkteamResponse:
    out: ListLabelingJobsForWorkteamResponse = {}  # type: ignore[typeddict-item]
    if "LabelingJobSummaryList" in data:
        import aws_sdk_sagemaker.types.labeling_job_for_workteam_summary_list

        out["labeling_job_summary_list"] = (
            aws_sdk_sagemaker.types.labeling_job_for_workteam_summary_list.deserialize_aws_json_1_1(
                data["LabelingJobSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
