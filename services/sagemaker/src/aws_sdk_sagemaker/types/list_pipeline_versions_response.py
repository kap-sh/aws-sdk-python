"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPipelineVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.pipeline_version_summary_list


class ListPipelineVersionsResponse(TypedDict):
    pipeline_version_summaries: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_summary_list.PipelineVersionSummaryList"
    ]
    """<p>Contains a sorted list of pipeline version summary objects matching the specified filters. Each version summary includes the pipeline version ID, the creation date, and the last pipeline execution created from that version. This list can be empty.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListPipelineVersions</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of pipeline versions, use this token in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelineVersionsResponse) -> dict:
    out: dict = {}
    if "pipeline_version_summaries" in value:
        import aws_sdk_sagemaker.types.pipeline_version_summary_list

        out["PipelineVersionSummaries"] = (
            aws_sdk_sagemaker.types.pipeline_version_summary_list.serialize_aws_json_1_1(
                value["pipeline_version_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelineVersionsResponse:
    out: ListPipelineVersionsResponse = {}  # type: ignore[typeddict-item]
    if "PipelineVersionSummaries" in data:
        import aws_sdk_sagemaker.types.pipeline_version_summary_list

        out["pipeline_version_summaries"] = (
            aws_sdk_sagemaker.types.pipeline_version_summary_list.deserialize_aws_json_1_1(
                data["PipelineVersionSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
