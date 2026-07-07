"""Generated from Smithy shape ``com.amazonaws.transfer#ImportSshPublicKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.server_id
    import aws_sdk_transfer.types.ssh_public_key_id
    import aws_sdk_transfer.types.user_name


class ImportSshPublicKeyResponse(TypedDict, closed=True):
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server.</p>"""
    ssh_public_key_id: "aws_sdk_transfer.types.ssh_public_key_id.SshPublicKeyId"
    """<p>The name given to a public key by the system that was imported.</p>"""
    user_name: "aws_sdk_transfer.types.user_name.UserName"
    """<p>A user name assigned to the <code>ServerID</code> value that you specified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportSshPublicKeyResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["SshPublicKeyId"] = value["ssh_public_key_id"]
    out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportSshPublicKeyResponse:
    out: ImportSshPublicKeyResponse = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ImportSshPublicKeyResponse.server_id required")
    if "SshPublicKeyId" in data:
        out["ssh_public_key_id"] = data["SshPublicKeyId"]
    else:
        raise DeserializationError(
            "ImportSshPublicKeyResponse.ssh_public_key_id required"
        )
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("ImportSshPublicKeyResponse.user_name required")
    return out
