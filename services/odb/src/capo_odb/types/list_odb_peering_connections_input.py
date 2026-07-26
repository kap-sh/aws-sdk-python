"""Generated from Smithy shape ``com.amazonaws.odb#ListOdbPeeringConnectionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class ListOdbPeeringConnectionsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of ODB peering connections to return in the response.</p> <p>Default: <code>20</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be between 1 and 100.</p> </li> </ul>"""
    next_token: NotRequired["str"]
    """<p>The pagination token for the next page of ODB peering connections.</p>"""
    odb_network_id: NotRequired["capo_odb.types.resource_id_or_arn.ResourceIdOrArn"]
    """<p>The identifier of the ODB network to list peering connections for.</p> <p>If not specified, lists all ODB peering connections in the account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOdbPeeringConnectionsInput) -> dict:
    out: dict = {}
    if "odb_network_id" in value:
        out["odbNetworkId"] = value["odb_network_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOdbPeeringConnectionsInput:
    out: ListOdbPeeringConnectionsInput = {}  # type: ignore[typeddict-item]
    if "odbNetworkId" in data:
        out["odb_network_id"] = data["odbNetworkId"]
    return out
