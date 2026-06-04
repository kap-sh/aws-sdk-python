"""Generated from Smithy shape ``com.amazonaws.iam#UploadSSHPublicKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.ssh_public_key


class UploadSSHPublicKeyResponse(TypedDict):
    ssh_public_key: NotRequired["aws_sdk_iam.types.ssh_public_key.SSHPublicKey"]
    """<p>Contains information about the SSH public key.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UploadSSHPublicKeyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ssh_public_key" in value:
        import aws_sdk_iam.types.ssh_public_key

        aws_sdk_iam.types.ssh_public_key.serialize_query(
            value["ssh_public_key"], pairs, f"{prefix}.SSHPublicKey"
        )


def deserialize_query(el: Element) -> UploadSSHPublicKeyResponse:
    out: UploadSSHPublicKeyResponse = {}  # type: ignore[typeddict-item]
    child_ssh_public_key = el.find("SSHPublicKey")
    if child_ssh_public_key is not None:
        import aws_sdk_iam.types.ssh_public_key

        out["ssh_public_key"] = aws_sdk_iam.types.ssh_public_key.deserialize_query(
            child_ssh_public_key
        )
    return out
