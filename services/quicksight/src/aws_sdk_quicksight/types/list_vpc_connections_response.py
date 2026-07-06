"""Generated from Smithy shape ``com.amazonaws.quicksight#ListVPCConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.vpc_connection_summary_list


class ListVPCConnectionsResponse(TypedDict, closed=True):
    vpc_connection_summaries: NotRequired[
        "aws_sdk_quicksight.types.vpc_connection_summary_list.VPCConnectionSummaryList"
    ]
    """<p>A <code>VPCConnectionSummaries</code> object that returns a summary of VPC connection objects.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVPCConnectionsResponse) -> dict:
    out: dict = {}
    if "vpc_connection_summaries" in value:
        import aws_sdk_quicksight.types.vpc_connection_summary_list

        out["VPCConnectionSummaries"] = (
            aws_sdk_quicksight.types.vpc_connection_summary_list.serialize_json(
                value["vpc_connection_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListVPCConnectionsResponse:
    out: ListVPCConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "VPCConnectionSummaries" in data:
        import aws_sdk_quicksight.types.vpc_connection_summary_list

        out["vpc_connection_summaries"] = (
            aws_sdk_quicksight.types.vpc_connection_summary_list.deserialize_json(
                data["VPCConnectionSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
