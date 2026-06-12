"""Generated from Smithy shape ``com.amazonaws.osis#ListPipelineEndpointConnectionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_osis.types.next_token
    import aws_sdk_osis.types.pipeline_endpoint_connections_summary_list


class ListPipelineEndpointConnectionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_osis.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    pipeline_endpoint_connections: NotRequired[
        "aws_sdk_osis.types.pipeline_endpoint_connections_summary_list.PipelineEndpointConnectionsSummaryList"
    ]
    """<p>A list of pipeline endpoint connections.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelineEndpointConnectionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "pipeline_endpoint_connections" in value:
        import aws_sdk_osis.types.pipeline_endpoint_connections_summary_list

        out["PipelineEndpointConnections"] = (
            aws_sdk_osis.types.pipeline_endpoint_connections_summary_list.serialize_json(
                value["pipeline_endpoint_connections"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPipelineEndpointConnectionsResponse:
    out: ListPipelineEndpointConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PipelineEndpointConnections" in data:
        import aws_sdk_osis.types.pipeline_endpoint_connections_summary_list

        out["pipeline_endpoint_connections"] = (
            aws_sdk_osis.types.pipeline_endpoint_connections_summary_list.deserialize_json(
                data["PipelineEndpointConnections"]
            )
        )
    return out
