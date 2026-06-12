"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListRuleExecutionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.max_results
    import aws_sdk_codepipeline.types.next_token
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.rule_execution_filter


class ListRuleExecutionsInput(TypedDict):
    pipeline_name: "aws_sdk_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline for which you want to get execution summary information.</p>"""
    filter: NotRequired[
        "aws_sdk_codepipeline.types.rule_execution_filter.RuleExecutionFilter"
    ]
    """<p>Input information used to filter rule execution history.</p>"""
    max_results: NotRequired["aws_sdk_codepipeline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Pipeline history is limited to the most recent 12 months, based on pipeline execution start times. Default value is 100.</p>"""
    next_token: NotRequired["aws_sdk_codepipeline.types.next_token.NextToken"]
    """<p>The token that was returned from the previous <code>ListRuleExecutions</code> call, which can be used to return the next set of rule executions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRuleExecutionsInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    if "filter" in value:
        import aws_sdk_codepipeline.types.rule_execution_filter

        out["filter"] = (
            aws_sdk_codepipeline.types.rule_execution_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRuleExecutionsInput:
    out: ListRuleExecutionsInput = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("ListRuleExecutionsInput.pipeline_name required")
    if "filter" in data:
        import aws_sdk_codepipeline.types.rule_execution_filter

        out["filter"] = (
            aws_sdk_codepipeline.types.rule_execution_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
