"""Generated from Smithy shape ``com.amazonaws.directconnect#DisassociateConnectionFromLagRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.lag_id


class DisassociateConnectionFromLagRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""
    lag_id: "capo_direct_connect.types.lag_id.LagId"
    """<p>The ID of the LAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateConnectionFromLagRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["lagId"] = value["lag_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateConnectionFromLagRequest:
    out: DisassociateConnectionFromLagRequest = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError(
            "DisassociateConnectionFromLagRequest.connection_id required"
        )
    if "lagId" in data:
        out["lag_id"] = data["lagId"]
    else:
        raise DeserializationError(
            "DisassociateConnectionFromLagRequest.lag_id required"
        )
    return out
