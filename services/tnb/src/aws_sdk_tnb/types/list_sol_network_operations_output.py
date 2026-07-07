"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkOperationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.list_sol_network_operations_resources
    import aws_sdk_tnb.types.pagination_token


class ListSolNetworkOperationsOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_tnb.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    network_operations: NotRequired[
        "aws_sdk_tnb.types.list_sol_network_operations_resources.ListSolNetworkOperationsResources"
    ]
    """<p>Lists network operation occurrences. Lifecycle management operations are deploy, update, or delete operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkOperationsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "network_operations" in value:
        import aws_sdk_tnb.types.list_sol_network_operations_resources

        out["networkOperations"] = (
            aws_sdk_tnb.types.list_sol_network_operations_resources.serialize_json(
                value["network_operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSolNetworkOperationsOutput:
    out: ListSolNetworkOperationsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "networkOperations" in data:
        import aws_sdk_tnb.types.list_sol_network_operations_resources

        out["network_operations"] = (
            aws_sdk_tnb.types.list_sol_network_operations_resources.deserialize_json(
                data["networkOperations"]
            )
        )
    return out
