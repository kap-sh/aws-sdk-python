"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#ListTunnelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.next_token
    import capo_iotsecuretunneling.types.tunnel_summary_list


class ListTunnelsResponse(TypedDict, closed=True):
    tunnel_summaries: NotRequired[
        "capo_iotsecuretunneling.types.tunnel_summary_list.TunnelSummaryList"
    ]
    """<p>A short description of the tunnels in an Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_iotsecuretunneling.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or null if there are no additional results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTunnelsResponse) -> dict:
    out: dict = {}
    if "tunnel_summaries" in value:
        import capo_iotsecuretunneling.types.tunnel_summary_list

        out["tunnelSummaries"] = (
            capo_iotsecuretunneling.types.tunnel_summary_list.serialize_aws_json_1_1(
                value["tunnel_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTunnelsResponse:
    out: ListTunnelsResponse = {}  # type: ignore[typeddict-item]
    if "tunnelSummaries" in data:
        import capo_iotsecuretunneling.types.tunnel_summary_list

        out["tunnel_summaries"] = (
            capo_iotsecuretunneling.types.tunnel_summary_list.deserialize_aws_json_1_1(
                data["tunnelSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
