"""Generated from Smithy shape ``com.amazonaws.mgn#DeleteVcenterClientRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_mgn.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_mgn.types.vcenter_client_id

class DeleteVcenterClientRequest(TypedDict):
    vcenter_client_id: "aws_sdk_mgn.types.vcenter_client_id.VcenterClientID"
    """<p>ID of resource to be deleted.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteVcenterClientRequest) -> dict:
    out: dict = {}
    out["vcenterClientID"] = value["vcenter_client_id"]
    return out


def deserialize_json(data: dict) -> DeleteVcenterClientRequest:
    out: DeleteVcenterClientRequest = {}  # type: ignore[typeddict-item]
    if "vcenterClientID" in data:
        out["vcenter_client_id"] = data["vcenterClientID"]
    else:
        raise DeserializationError("DeleteVcenterClientRequest.vcenter_client_id required")
    return out