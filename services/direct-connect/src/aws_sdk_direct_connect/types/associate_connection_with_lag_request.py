"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociateConnectionWithLagRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.lag_id


class AssociateConnectionWithLagRequest(TypedDict, closed=True):
    connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""
    lag_id: "aws_sdk_direct_connect.types.lag_id.LagId"
    """<p>The ID of the LAG with which to associate the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateConnectionWithLagRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["lagId"] = value["lag_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateConnectionWithLagRequest:
    out: AssociateConnectionWithLagRequest = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError(
            "AssociateConnectionWithLagRequest.connection_id required"
        )
    if "lagId" in data:
        out["lag_id"] = data["lagId"]
    else:
        raise DeserializationError("AssociateConnectionWithLagRequest.lag_id required")
    return out
