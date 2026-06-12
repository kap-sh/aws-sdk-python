"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociateHostedConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection_id


class AssociateHostedConnectionRequest(TypedDict):
    connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the hosted connection.</p>"""
    parent_connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the interconnect or the LAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateHostedConnectionRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["parentConnectionId"] = value["parent_connection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateHostedConnectionRequest:
    out: AssociateHostedConnectionRequest = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError(
            "AssociateHostedConnectionRequest.connection_id required"
        )
    if "parentConnectionId" in data:
        out["parent_connection_id"] = data["parentConnectionId"]
    else:
        raise DeserializationError(
            "AssociateHostedConnectionRequest.parent_connection_id required"
        )
    return out
