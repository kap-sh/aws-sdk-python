"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelQualityJobDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_job_definition_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListModelQualityJobDefinitionsResponse(TypedDict, closed=True):
    job_definition_summaries: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition_summary_list.MonitoringJobDefinitionSummaryList"
    ]
    """<p>A list of summaries of model quality monitoring job definitions.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker AI returns this token. To retrieve the next set of model quality monitoring job definitions, use it in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelQualityJobDefinitionsResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ListModelQualityJobDefinitionsResponse:
    out: ListModelQualityJobDefinitionsResponse = {}  # type: ignore[typeddict-item]
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
