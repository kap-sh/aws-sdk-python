"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListDataQualityJobDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_job_definition_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListDataQualityJobDefinitionsResponse(TypedDict):
    job_definition_summaries: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition_summary_list.MonitoringJobDefinitionSummaryList"
    ]
    """<p>A list of data quality monitoring job definitions.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListDataQualityJobDefinitions</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of data quality monitoring job definitions, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityJobDefinitionsResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityJobDefinitionsResponse:
    out: ListDataQualityJobDefinitionsResponse = {}  # type: ignore[typeddict-item]
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
