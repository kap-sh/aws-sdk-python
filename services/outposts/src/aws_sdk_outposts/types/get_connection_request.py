"""Generated from Smithy shape ``com.amazonaws.outposts#GetConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.connection_id


class GetConnectionRequest(TypedDict):
    connection_id: "aws_sdk_outposts.types.connection_id.ConnectionId"
    """<p> The ID of the connection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectionRequest:
    out: GetConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
