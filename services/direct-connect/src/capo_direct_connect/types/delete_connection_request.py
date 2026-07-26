"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id


class DeleteConnectionRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectionRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConnectionRequest:
    out: DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError("DeleteConnectionRequest.connection_id required")
    return out
