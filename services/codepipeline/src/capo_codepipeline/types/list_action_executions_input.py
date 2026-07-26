"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListActionExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_execution_filter
    import capo_codepipeline.types.max_results
    import capo_codepipeline.types.next_token
    import capo_codepipeline.types.pipeline_name


class ListActionExecutionsInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p> The name of the pipeline for which you want to list action execution history.</p>"""
    filter: NotRequired[
        "capo_codepipeline.types.action_execution_filter.ActionExecutionFilter"
    ]
    """<p>Input information used to filter action execution history.</p>"""
    max_results: NotRequired["capo_codepipeline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Action execution history is retained for up to 12 months, based on action execution start times. Default value is 100. </p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>The token that was returned from the previous <code>ListActionExecutions</code> call, which can be used to return the next set of action executions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListActionExecutionsInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    if "filter" in value:
        import capo_codepipeline.types.action_execution_filter

        out["filter"] = (
            capo_codepipeline.types.action_execution_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListActionExecutionsInput:
    out: ListActionExecutionsInput = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("ListActionExecutionsInput.pipeline_name required")
    if "filter" in data:
        import capo_codepipeline.types.action_execution_filter

        out["filter"] = (
            capo_codepipeline.types.action_execution_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
