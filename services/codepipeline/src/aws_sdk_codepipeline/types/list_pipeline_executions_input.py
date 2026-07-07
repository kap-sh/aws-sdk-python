"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListPipelineExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.max_results
    import aws_sdk_codepipeline.types.next_token
    import aws_sdk_codepipeline.types.pipeline_execution_filter
    import aws_sdk_codepipeline.types.pipeline_name


class ListPipelineExecutionsInput(TypedDict, closed=True):
    pipeline_name: "aws_sdk_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline for which you want to get execution summary information.</p>"""
    max_results: NotRequired["aws_sdk_codepipeline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Pipeline history is limited to the most recent 12 months, based on pipeline execution start times. Default value is 100.</p>"""
    filter: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_execution_filter.PipelineExecutionFilter"
    ]
    """<p>The pipeline execution to filter on.</p>"""
    next_token: NotRequired["aws_sdk_codepipeline.types.next_token.NextToken"]
    """<p>The token that was returned from the previous <code>ListPipelineExecutions</code> call, which can be used to return the next set of pipeline executions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelineExecutionsInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import aws_sdk_codepipeline.types.pipeline_execution_filter

        out["filter"] = (
            aws_sdk_codepipeline.types.pipeline_execution_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelineExecutionsInput:
    out: ListPipelineExecutionsInput = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("ListPipelineExecutionsInput.pipeline_name required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filter" in data:
        import aws_sdk_codepipeline.types.pipeline_execution_filter

        out["filter"] = (
            aws_sdk_codepipeline.types.pipeline_execution_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
