"""Generated from Smithy shape ``com.amazonaws.iam#UpdateSSHPublicKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.public_key_id_type
    import aws_sdk_iam.types.status_type
    import aws_sdk_iam.types.user_name_type


class UpdateSSHPublicKeyRequest(TypedDict):
    user_name: "aws_sdk_iam.types.user_name_type.userNameType"
    r"""<p>The name of the IAM user associated with the SSH public key.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    ssh_public_key_id: "aws_sdk_iam.types.public_key_id_type.publicKeyIdType"
    r"""<p>The unique identifier for the SSH public key.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters that can consist of any upper or lowercased letter or digit.</p>"""
    status: "aws_sdk_iam.types.status_type.statusType"
    """<p>The status to assign to the SSH public key. <code>Active</code> means that the key can be used for authentication with an CodeCommit repository. <code>Inactive</code> means that the key cannot be used.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateSSHPublicKeyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    pairs.append((f"{prefix}.SSHPublicKeyId", str(value["ssh_public_key_id"])))
    import aws_sdk_iam.types.status_type

    aws_sdk_iam.types.status_type.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )


def deserialize_query(el: Element) -> UpdateSSHPublicKeyRequest:
    out: UpdateSSHPublicKeyRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("UpdateSSHPublicKeyRequest.user_name required")
    child_ssh_public_key_id = el.find("SSHPublicKeyId")
    if child_ssh_public_key_id is not None:
        out["ssh_public_key_id"] = str(child_ssh_public_key_id.text or "")
    else:
        raise DeserializationError(
            "UpdateSSHPublicKeyRequest.ssh_public_key_id required"
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_iam.types.status_type

        out["status"] = aws_sdk_iam.types.status_type.deserialize_query(child_status)
    else:
        raise DeserializationError("UpdateSSHPublicKeyRequest.status required")
    return out
