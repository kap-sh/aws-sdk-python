"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.server_id


class DeleteServerRequest(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A unique system-assigned identifier for a server instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteServerRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteServerRequest:
    out: DeleteServerRequest = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("DeleteServerRequest.server_id required")
    return out
