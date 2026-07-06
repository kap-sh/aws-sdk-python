"""Generated from Smithy shape ``com.amazonaws.interconnect#ListConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.connection_summaries_list
    import aws_sdk_interconnect.types.next_token


class ListConnectionsResponse(TypedDict, closed=True):
    connections: NotRequired[
        "aws_sdk_interconnect.types.connection_summaries_list.ConnectionSummariesList"
    ]
    """<p>The resulting list of <a>Connection</a> objects.</p>"""
    next_token: NotRequired["aws_sdk_interconnect.types.next_token.NextToken"]
    """<p>A pagination token for use in subsequent calls to fetch the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsResponse) -> dict:
    out: dict = {}
    if "connections" in value:
        import aws_sdk_interconnect.types.connection_summaries_list

        out["connections"] = (
            aws_sdk_interconnect.types.connection_summaries_list.serialize_aws_json_1_0(
                value["connections"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsResponse:
    out: ListConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "connections" in data:
        import aws_sdk_interconnect.types.connection_summaries_list

        out["connections"] = (
            aws_sdk_interconnect.types.connection_summaries_list.deserialize_aws_json_1_0(
                data["connections"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
