"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelBiasJobDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_job_definition_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListModelBiasJobDefinitionsResponse(TypedDict, closed=True):
    job_definition_summaries: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition_summary_list.MonitoringJobDefinitionSummaryList"
    ]
    """<p>A JSON array in which each element is a summary for a model bias jobs.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelBiasJobDefinitionsResponse) -> dict:
    out: dict = {}
    if "job_definition_summaries" in value:
        import aws_sdk_sagemaker.types.monitoring_job_definition_summary_list

        out["JobDefinitionSummaries"] = (
            aws_sdk_sagemaker.types.monitoring_job_definition_summary_list.serialize_aws_json_1_1(
                value["job_definition_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelBiasJobDefinitionsResponse:
    out: ListModelBiasJobDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "JobDefinitionSummaries" in data:
        import aws_sdk_sagemaker.types.monitoring_job_definition_summary_list

        out["job_definition_summaries"] = (
            aws_sdk_sagemaker.types.monitoring_job_definition_summary_list.deserialize_aws_json_1_1(
                data["JobDefinitionSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
