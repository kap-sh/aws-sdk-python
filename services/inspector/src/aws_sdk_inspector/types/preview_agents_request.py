"""Generated from Smithy shape ``com.amazonaws.inspector#PreviewAgentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.pagination_token
    import aws_sdk_inspector.types.preview_agents_max_results


class PreviewAgentsRequest(TypedDict):
    preview_agents_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the assessment target whose agents you want to preview.</p>"""
    next_token: NotRequired["aws_sdk_inspector.types.pagination_token.PaginationToken"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>PreviewAgents</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>"""
    max_results: NotRequired[
        "aws_sdk_inspector.types.preview_agents_max_results.PreviewAgentsMaxResults"
    ]
    """<p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreviewAgentsRequest) -> dict:
    out: dict = {}
    out["previewAgentsArn"] = value["preview_agents_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PreviewAgentsRequest:
    out: PreviewAgentsRequest = {}  # type: ignore[typeddict-item]
    if "previewAgentsArn" in data:
        out["preview_agents_arn"] = data["previewAgentsArn"]
    else:
        raise DeserializationError("PreviewAgentsRequest.preview_agents_arn required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
