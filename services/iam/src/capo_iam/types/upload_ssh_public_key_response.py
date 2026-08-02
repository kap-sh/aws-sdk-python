"""Generated from Smithy shape ``com.amazonaws.iam#UploadSSHPublicKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.ssh_public_key


class UploadSSHPublicKeyResponse(TypedDict, closed=True):
    ssh_public_key: NotRequired["capo_iam.types.ssh_public_key.SSHPublicKey"]
    """<p>Contains information about the SSH public key.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UploadSSHPublicKeyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ssh_public_key" in value:
        import capo_iam.types.ssh_public_key

        capo_iam.types.ssh_public_key.serialize_query(
            value["ssh_public_key"], pairs, f"{key_prefix}SSHPublicKey"
        )


def deserialize_query(el: Element) -> UploadSSHPublicKeyResponse:
    out: UploadSSHPublicKeyResponse = {}  # type: ignore[typeddict-item]
    child_ssh_public_key = el.find("SSHPublicKey")
    if child_ssh_public_key is not None:
        import capo_iam.types.ssh_public_key

        out["ssh_public_key"] = capo_iam.types.ssh_public_key.deserialize_query(
            child_ssh_public_key
        )
    return out
