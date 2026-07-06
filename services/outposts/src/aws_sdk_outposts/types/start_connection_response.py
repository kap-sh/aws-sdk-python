"""Generated from Smithy shape ``com.amazonaws.outposts#StartConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.connection_id
    import aws_sdk_outposts.types.underlay_ip_address


class StartConnectionResponse(TypedDict, closed=True):
    connection_id: NotRequired["aws_sdk_outposts.types.connection_id.ConnectionId"]
    """<p> The ID of the connection. </p>"""
    underlay_ip_address: NotRequired[
        "aws_sdk_outposts.types.underlay_ip_address.UnderlayIpAddress"
    ]
    """<p> The underlay IP address. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartConnectionResponse) -> dict:
    out: dict = {}
    if "connection_id" in value:
        out["ConnectionId"] = value["connection_id"]
    if "underlay_ip_address" in value:
        out["UnderlayIpAddress"] = value["underlay_ip_address"]
    return out


def deserialize_json(data: dict) -> StartConnectionResponse:
    out: StartConnectionResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionId" in data:
        out["connection_id"] = data["ConnectionId"]
    if "UnderlayIpAddress" in data:
        out["underlay_ip_address"] = data["UnderlayIpAddress"]
    return out
