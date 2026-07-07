"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.list_sol_network_instance_resources
    import aws_sdk_tnb.types.pagination_token


class ListSolNetworkInstancesOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_tnb.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    network_instances: NotRequired[
        "aws_sdk_tnb.types.list_sol_network_instance_resources.ListSolNetworkInstanceResources"
    ]
    """<p>Lists network instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkInstancesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "network_instances" in value:
        import aws_sdk_tnb.types.list_sol_network_instance_resources

        out["networkInstances"] = (
            aws_sdk_tnb.types.list_sol_network_instance_resources.serialize_json(
                value["network_instances"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSolNetworkInstancesOutput:
    out: ListSolNetworkInstancesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "networkInstances" in data:
        import aws_sdk_tnb.types.list_sol_network_instance_resources

        out["network_instances"] = (
            aws_sdk_tnb.types.list_sol_network_instance_resources.deserialize_json(
                data["networkInstances"]
            )
        )
    return out
