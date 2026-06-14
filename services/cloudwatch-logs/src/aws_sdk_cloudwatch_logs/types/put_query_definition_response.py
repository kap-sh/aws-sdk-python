"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutQueryDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.query_id


class PutQueryDefinitionResponse(TypedDict):
    query_definition_id: NotRequired["aws_sdk_cloudwatch_logs.types.query_id.QueryId"]
    """<p>The ID of the query definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutQueryDefinitionResponse) -> dict:
    out: dict = {}
    if "query_definition_id" in value:
        out["queryDefinitionId"] = value["query_definition_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutQueryDefinitionResponse:
    out: PutQueryDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "queryDefinitionId" in data:
        out["query_definition_id"] = data["queryDefinitionId"]
    return out
