"""Generated from Smithy shape ``com.amazonaws.outposts#GetConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.connection_details
    import capo_outposts.types.connection_id


class GetConnectionResponse(TypedDict, closed=True):
    connection_id: NotRequired["capo_outposts.types.connection_id.ConnectionId"]
    """<p> The ID of the connection. </p>"""
    connection_details: NotRequired[
        "capo_outposts.types.connection_details.ConnectionDetails"
    ]
    """<p> Information about the connection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionResponse) -> dict:
    out: dict = {}
    if "connection_id" in value:
        out["ConnectionId"] = value["connection_id"]
    if "connection_details" in value:
        import capo_outposts.types.connection_details

        out["ConnectionDetails"] = (
            capo_outposts.types.connection_details.serialize_json(
                value["connection_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConnectionResponse:
    out: GetConnectionResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionId" in data:
        out["connection_id"] = data["ConnectionId"]
    if "ConnectionDetails" in data:
        import capo_outposts.types.connection_details

        out["connection_details"] = (
            capo_outposts.types.connection_details.deserialize_json(
                data["ConnectionDetails"]
            )
        )
    return out
