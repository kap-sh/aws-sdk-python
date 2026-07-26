"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeQueryDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.query_definition_list


class DescribeQueryDefinitionsResponse(TypedDict, closed=True):
    query_definitions: NotRequired[
        "capo_cloudwatch_logs.types.query_definition_list.QueryDefinitionList"
    ]
    """<p>The list of query definitions that match your request.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQueryDefinitionsResponse) -> dict:
    out: dict = {}
    if "query_definitions" in value:
        import capo_cloudwatch_logs.types.query_definition_list

        out["queryDefinitions"] = (
            capo_cloudwatch_logs.types.query_definition_list.serialize_aws_json_1_1(
                value["query_definitions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQueryDefinitionsResponse:
    out: DescribeQueryDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "queryDefinitions" in data:
        import capo_cloudwatch_logs.types.query_definition_list

        out["query_definitions"] = (
            capo_cloudwatch_logs.types.query_definition_list.deserialize_aws_json_1_1(
                data["queryDefinitions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
