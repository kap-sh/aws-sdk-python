"""Generated from Smithy shape ``com.amazonaws.transfer#ImportSshPublicKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.server_id
    import capo_transfer.types.ssh_public_key_body
    import capo_transfer.types.user_name


class ImportSshPublicKeyRequest(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server.</p>"""
    ssh_public_key_body: "capo_transfer.types.ssh_public_key_body.SshPublicKeyBody"
    """<p>The public key portion of an SSH key pair.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p>"""
    user_name: "capo_transfer.types.user_name.UserName"
    """<p>The name of the Transfer Family user that is assigned to one or more servers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportSshPublicKeyRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["SshPublicKeyBody"] = value["ssh_public_key_body"]
    out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportSshPublicKeyRequest:
    out: ImportSshPublicKeyRequest = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ImportSshPublicKeyRequest.server_id required")
    if "SshPublicKeyBody" in data:
        out["ssh_public_key_body"] = data["SshPublicKeyBody"]
    else:
        raise DeserializationError(
            "ImportSshPublicKeyRequest.ssh_public_key_body required"
        )
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("ImportSshPublicKeyRequest.user_name required")
    return out
