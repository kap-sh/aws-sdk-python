"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceTopologyEdgeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_topology_edge_summary

ServiceTopologyEdgeSummaryList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.service_topology_edge_summary.ServiceTopologyEdgeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceTopologyEdgeSummaryList) -> list:
    import aws_sdk_resiliencehubv2.types.service_topology_edge_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehubv2.types.service_topology_edge_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServiceTopologyEdgeSummaryList:
    import aws_sdk_resiliencehubv2.types.service_topology_edge_summary

    out: ServiceTopologyEdgeSummaryList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.service_topology_edge_summary.deserialize_json(
                item
            )
        )
    return out
