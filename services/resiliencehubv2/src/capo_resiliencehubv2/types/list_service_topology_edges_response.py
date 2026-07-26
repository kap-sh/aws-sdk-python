"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListServiceTopologyEdgesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.service_topology_edge_summary_list


class ListServiceTopologyEdgesResponse(TypedDict, closed=True):
    service_topology_edge_summaries: NotRequired[
        "capo_resiliencehubv2.types.service_topology_edge_summary_list.ServiceTopologyEdgeSummaryList"
    ]
    """<p>The list of service topology edge summaries.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceTopologyEdgesResponse) -> dict:
    out: dict = {}
    if "service_topology_edge_summaries" in value:
        import capo_resiliencehubv2.types.service_topology_edge_summary_list

        out["serviceTopologyEdgeSummaries"] = (
            capo_resiliencehubv2.types.service_topology_edge_summary_list.serialize_json(
                value["service_topology_edge_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceTopologyEdgesResponse:
    out: ListServiceTopologyEdgesResponse = {}  # type: ignore[typeddict-item]
    if "serviceTopologyEdgeSummaries" in data:
        import capo_resiliencehubv2.types.service_topology_edge_summary_list

        out["service_topology_edge_summaries"] = (
            capo_resiliencehubv2.types.service_topology_edge_summary_list.deserialize_json(
                data["serviceTopologyEdgeSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
