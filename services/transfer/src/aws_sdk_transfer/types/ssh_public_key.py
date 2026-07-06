"""Generated from Smithy shape ``com.amazonaws.transfer#SshPublicKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.date_imported
    import aws_sdk_transfer.types.ssh_public_key_body
    import aws_sdk_transfer.types.ssh_public_key_id


class SshPublicKey(TypedDict, closed=True):
    date_imported: "aws_sdk_transfer.types.date_imported.DateImported"
    """<p>Specifies the date that the public key was added to the Transfer Family user.</p>"""
    ssh_public_key_body: "aws_sdk_transfer.types.ssh_public_key_body.SshPublicKeyBody"
    """<p>Specifies the content of the SSH public key as specified by the <code>PublicKeyId</code>.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p>"""
    ssh_public_key_id: "aws_sdk_transfer.types.ssh_public_key_id.SshPublicKeyId"
    """<p>Specifies the <code>SshPublicKeyId</code> parameter contains the identifier of the public key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SshPublicKey) -> dict:
    out: dict = {}
    import aws_sdk_transfer.types.date_imported

    out["DateImported"] = aws_sdk_transfer.types.date_imported.serialize_aws_json_1_1(
        value["date_imported"]
    )
    out["SshPublicKeyBody"] = value["ssh_public_key_body"]
    out["SshPublicKeyId"] = value["ssh_public_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SshPublicKey:
    out: SshPublicKey = {}  # type: ignore[typeddict-item]
    if "DateImported" in data:
        import aws_sdk_transfer.types.date_imported

        out["date_imported"] = (
            aws_sdk_transfer.types.date_imported.deserialize_aws_json_1_1(
                data["DateImported"]
            )
        )
    else:
        raise DeserializationError("SshPublicKey.date_imported required")
    if "SshPublicKeyBody" in data:
        out["ssh_public_key_body"] = data["SshPublicKeyBody"]
    else:
        raise DeserializationError("SshPublicKey.ssh_public_key_body required")
    if "SshPublicKeyId" in data:
        out["ssh_public_key_id"] = data["SshPublicKeyId"]
    else:
        raise DeserializationError("SshPublicKey.ssh_public_key_id required")
    return out
