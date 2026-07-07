"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListPrivateGraphEndpointsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.pagination_token
    import aws_sdk_neptune_graph.types.private_graph_endpoint_summary_list


class ListPrivateGraphEndpointsOutput(TypedDict, closed=True):
    private_graph_endpoints: "aws_sdk_neptune_graph.types.private_graph_endpoint_summary_list.PrivateGraphEndpointSummaryList"
    """<p>A list of private endpoints for the specified Neptune Analytics graph.</p>"""
    next_token: NotRequired[
        "aws_sdk_neptune_graph.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivateGraphEndpointsOutput) -> dict:
    out: dict = {}
    import aws_sdk_neptune_graph.types.private_graph_endpoint_summary_list

    out["privateGraphEndpoints"] = (
        aws_sdk_neptune_graph.types.private_graph_endpoint_summary_list.serialize_json(
            value["private_graph_endpoints"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPrivateGraphEndpointsOutput:
    out: ListPrivateGraphEndpointsOutput = {}  # type: ignore[typeddict-item]
    if "privateGraphEndpoints" in data:
        import aws_sdk_neptune_graph.types.private_graph_endpoint_summary_list

        out["private_graph_endpoints"] = (
            aws_sdk_neptune_graph.types.private_graph_endpoint_summary_list.deserialize_json(
                data["privateGraphEndpoints"]
            )
        )
    else:
        raise DeserializationError(
            "ListPrivateGraphEndpointsOutput.private_graph_endpoints required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
