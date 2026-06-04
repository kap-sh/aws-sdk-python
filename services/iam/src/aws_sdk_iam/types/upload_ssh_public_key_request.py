"""Generated from Smithy shape ``com.amazonaws.iam#UploadSSHPublicKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.public_key_material_type
    import aws_sdk_iam.types.user_name_type


class UploadSSHPublicKeyRequest(TypedDict):
    user_name: "aws_sdk_iam.types.user_name_type.userNameType"
    """<p>The name of the IAM user to associate the SSH public key with.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    ssh_public_key_body: (
        "aws_sdk_iam.types.public_key_material_type.publicKeyMaterialType"
    )
    """<p>The SSH public key. The public key must be encoded in ssh-rsa format or PEM format. The minimum bit-length of the public key is 2048 bits. For example, you can generate a 2048-bit key, and the resulting PEM file is 1679 bytes long.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00ff</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000a</code>), and carriage return (<code>\u000d</code>)</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UploadSSHPublicKeyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    pairs.append((f"{prefix}.SSHPublicKeyBody", str(value["ssh_public_key_body"])))


def deserialize_query(el: Element) -> UploadSSHPublicKeyRequest:
    out: UploadSSHPublicKeyRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("UploadSSHPublicKeyRequest.user_name required")
    child_ssh_public_key_body = el.find("SSHPublicKeyBody")
    if child_ssh_public_key_body is not None:
        out["ssh_public_key_body"] = str(child_ssh_public_key_body.text or "")
    else:
        raise DeserializationError(
            "UploadSSHPublicKeyRequest.ssh_public_key_body required"
        )
    return out
