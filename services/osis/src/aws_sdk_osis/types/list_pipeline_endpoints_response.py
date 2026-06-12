"""Generated from Smithy shape ``com.amazonaws.osis#ListPipelineEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_osis.types.next_token
    import aws_sdk_osis.types.pipeline_endpoints_summary_list


class ListPipelineEndpointsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_osis.types.next_token.NextToken"]
    """<p>When <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    pipeline_endpoints: NotRequired[
        "aws_sdk_osis.types.pipeline_endpoints_summary_list.PipelineEndpointsSummaryList"
    ]
    """<p>A list of pipeline endpoints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelineEndpointsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "pipeline_endpoints" in value:
        import aws_sdk_osis.types.pipeline_endpoints_summary_list

        out["PipelineEndpoints"] = (
            aws_sdk_osis.types.pipeline_endpoints_summary_list.serialize_json(
                value["pipeline_endpoints"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPipelineEndpointsResponse:
    out: ListPipelineEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PipelineEndpoints" in data:
        import aws_sdk_osis.types.pipeline_endpoints_summary_list

        out["pipeline_endpoints"] = (
            aws_sdk_osis.types.pipeline_endpoints_summary_list.deserialize_json(
                data["PipelineEndpoints"]
            )
        )
    return out
