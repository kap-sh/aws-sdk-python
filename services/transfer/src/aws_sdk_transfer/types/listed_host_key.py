"""Generated from Smithy shape ``com.amazonaws.transfer#ListedHostKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.date_imported
    import aws_sdk_transfer.types.host_key_description
    import aws_sdk_transfer.types.host_key_fingerprint
    import aws_sdk_transfer.types.host_key_id
    import aws_sdk_transfer.types.host_key_type


class ListedHostKey(TypedDict):
    arn: "aws_sdk_transfer.types.arn.Arn"
    """<p>The unique Amazon Resource Name (ARN) of the host key.</p>"""
    host_key_id: NotRequired["aws_sdk_transfer.types.host_key_id.HostKeyId"]
    """<p>A unique identifier for the host key.</p>"""
    fingerprint: NotRequired[
        "aws_sdk_transfer.types.host_key_fingerprint.HostKeyFingerprint"
    ]
    """<p>The public key fingerprint, which is a short sequence of bytes used to identify the longer public key.</p>"""
    description: NotRequired[
        "aws_sdk_transfer.types.host_key_description.HostKeyDescription"
    ]
    """<p>The current description for the host key. You can change it by calling the <code>UpdateHostKey</code> operation and providing a new description.</p>"""
    type: NotRequired["aws_sdk_transfer.types.host_key_type.HostKeyType"]
    """<p>The encryption algorithm that is used for the host key. The <code>Type</code> parameter is specified by using one of the following values:</p> <ul> <li> <p> <code>ssh-rsa</code> </p> </li> <li> <p> <code>ssh-ed25519</code> </p> </li> <li> <p> <code>ecdsa-sha2-nistp256</code> </p> </li> <li> <p> <code>ecdsa-sha2-nistp384</code> </p> </li> <li> <p> <code>ecdsa-sha2-nistp521</code> </p> </li> </ul>"""
    date_imported: NotRequired["aws_sdk_transfer.types.date_imported.DateImported"]
    """<p>The date on which the host key was added to the server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedHostKey) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "host_key_id" in value:
        out["HostKeyId"] = value["host_key_id"]
    if "fingerprint" in value:
        out["Fingerprint"] = value["fingerprint"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    if "date_imported" in value:
        import aws_sdk_transfer.types.date_imported

        out["DateImported"] = (
            aws_sdk_transfer.types.date_imported.serialize_aws_json_1_1(
                value["date_imported"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedHostKey:
    out: ListedHostKey = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ListedHostKey.arn required")
    if "HostKeyId" in data:
        out["host_key_id"] = data["HostKeyId"]
    if "Fingerprint" in data:
        out["fingerprint"] = data["Fingerprint"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "DateImported" in data:
        import aws_sdk_transfer.types.date_imported

        out["date_imported"] = (
            aws_sdk_transfer.types.date_imported.deserialize_aws_json_1_1(
                data["DateImported"]
            )
        )
    return out
