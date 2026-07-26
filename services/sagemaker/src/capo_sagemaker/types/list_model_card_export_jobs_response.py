"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelCardExportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_card_export_job_summary_list
    import capo_sagemaker.types.next_token


class ListModelCardExportJobsResponse(TypedDict, closed=True):
    model_card_export_job_summaries: NotRequired[
        "capo_sagemaker.types.model_card_export_job_summary_list.ModelCardExportJobSummaryList"
    ]
    """<p>The summaries of the listed model card export jobs.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of model card export jobs, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelCardExportJobsResponse) -> dict:
    out: dict = {}
    if "model_card_export_job_summaries" in value:
        import capo_sagemaker.types.model_card_export_job_summary_list

        out["ModelCardExportJobSummaries"] = (
            capo_sagemaker.types.model_card_export_job_summary_list.serialize_aws_json_1_1(
                value["model_card_export_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelCardExportJobsResponse:
    out: ListModelCardExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "ModelCardExportJobSummaries" in data:
        import capo_sagemaker.types.model_card_export_job_summary_list

        out["model_card_export_job_summaries"] = (
            capo_sagemaker.types.model_card_export_job_summary_list.deserialize_aws_json_1_1(
                data["ModelCardExportJobSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
