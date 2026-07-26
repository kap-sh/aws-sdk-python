"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListPipelineExecutionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.next_token
    import capo_codepipeline.types.pipeline_execution_summary_list


class ListPipelineExecutionsOutput(TypedDict, closed=True):
    pipeline_execution_summaries: NotRequired[
        "capo_codepipeline.types.pipeline_execution_summary_list.PipelineExecutionSummaryList"
    ]
    """<p>A list of executions in the history of a pipeline.</p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>A token that can be used in the next <code>ListPipelineExecutions</code> call. To view all items in the list, continue to call this operation with each subsequent token until no more nextToken values are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelineExecutionsOutput) -> dict:
    out: dict = {}
    if "pipeline_execution_summaries" in value:
        import capo_codepipeline.types.pipeline_execution_summary_list

        out["pipelineExecutionSummaries"] = (
            capo_codepipeline.types.pipeline_execution_summary_list.serialize_aws_json_1_1(
                value["pipeline_execution_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelineExecutionsOutput:
    out: ListPipelineExecutionsOutput = {}  # type: ignore[typeddict-item]
    if "pipelineExecutionSummaries" in data:
        import capo_codepipeline.types.pipeline_execution_summary_list

        out["pipeline_execution_summaries"] = (
            capo_codepipeline.types.pipeline_execution_summary_list.deserialize_aws_json_1_1(
                data["pipelineExecutionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
