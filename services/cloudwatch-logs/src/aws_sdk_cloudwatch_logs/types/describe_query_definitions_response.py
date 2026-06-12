"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeQueryDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.query_definition_list


class DescribeQueryDefinitionsResponse(TypedDict):
    query_definitions: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_definition_list.QueryDefinitionList"
    ]
    """<p>The list of query definitions that match your request.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQueryDefinitionsResponse) -> dict:
    out: dict = {}
    if "query_definitions" in value:
        import aws_sdk_cloudwatch_logs.types.query_definition_list

        out["queryDefinitions"] = (
            aws_sdk_cloudwatch_logs.types.query_definition_list.serialize_aws_json_1_1(
                value["query_definitions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQueryDefinitionsResponse:
    out: DescribeQueryDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "queryDefinitions" in data:
        import aws_sdk_cloudwatch_logs.types.query_definition_list

        out["query_definitions"] = (
            aws_sdk_cloudwatch_logs.types.query_definition_list.deserialize_aws_json_1_1(
                data["queryDefinitions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
