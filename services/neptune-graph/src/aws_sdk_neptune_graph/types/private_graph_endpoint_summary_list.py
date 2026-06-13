"""Generated from Smithy shape ``com.amazonaws.neptunegraph#PrivateGraphEndpointSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.private_graph_endpoint_summary

PrivateGraphEndpointSummaryList: TypeAlias = list[
    "aws_sdk_neptune_graph.types.private_graph_endpoint_summary.PrivateGraphEndpointSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateGraphEndpointSummaryList) -> list:
    import aws_sdk_neptune_graph.types.private_graph_endpoint_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_neptune_graph.types.private_graph_endpoint_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PrivateGraphEndpointSummaryList:
    import aws_sdk_neptune_graph.types.private_graph_endpoint_summary

    out: PrivateGraphEndpointSummaryList = []
    for item in data:
        out.append(
            aws_sdk_neptune_graph.types.private_graph_endpoint_summary.deserialize_json(
                item
            )
        )
    return out
