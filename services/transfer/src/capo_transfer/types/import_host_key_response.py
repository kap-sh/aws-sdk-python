"""Generated from Smithy shape ``com.amazonaws.transfer#ImportHostKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.host_key_id
    import capo_transfer.types.server_id


class ImportHostKeyResponse(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>Returns the server identifier that contains the imported key.</p>"""
    host_key_id: "capo_transfer.types.host_key_id.HostKeyId"
    """<p>Returns the host key identifier for the imported key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportHostKeyResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["HostKeyId"] = value["host_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportHostKeyResponse:
    out: ImportHostKeyResponse = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ImportHostKeyResponse.server_id required")
    if "HostKeyId" in data:
        out["host_key_id"] = data["HostKeyId"]
    else:
        raise DeserializationError("ImportHostKeyResponse.host_key_id required")
    return out
