"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateHostKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.host_key_id
    import aws_sdk_transfer.types.server_id


class UpdateHostKeyResponse(TypedDict, closed=True):
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>Returns the server identifier for the server that contains the updated host key.</p>"""
    host_key_id: "aws_sdk_transfer.types.host_key_id.HostKeyId"
    """<p>Returns the host key identifier for the updated host key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHostKeyResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["HostKeyId"] = value["host_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHostKeyResponse:
    out: UpdateHostKeyResponse = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("UpdateHostKeyResponse.server_id required")
    if "HostKeyId" in data:
        out["host_key_id"] = data["HostKeyId"]
    else:
        raise DeserializationError("UpdateHostKeyResponse.host_key_id required")
    return out
