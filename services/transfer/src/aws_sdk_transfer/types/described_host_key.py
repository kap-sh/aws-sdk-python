"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedHostKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.date_imported
    import aws_sdk_transfer.types.host_key_description
    import aws_sdk_transfer.types.host_key_fingerprint
    import aws_sdk_transfer.types.host_key_id
    import aws_sdk_transfer.types.host_key_type
    import aws_sdk_transfer.types.tags


class DescribedHostKey(TypedDict, closed=True):
    arn: "aws_sdk_transfer.types.arn.Arn"
    """<p>The unique Amazon Resource Name (ARN) for the host key.</p>"""
    host_key_id: NotRequired["aws_sdk_transfer.types.host_key_id.HostKeyId"]
    """<p>A unique identifier for the host key.</p>"""
    host_key_fingerprint: NotRequired[
        "aws_sdk_transfer.types.host_key_fingerprint.HostKeyFingerprint"
    ]
    """<p>The public key fingerprint, which is a short sequence of bytes used to identify the longer public key.</p>"""
    description: NotRequired[
        "aws_sdk_transfer.types.host_key_description.HostKeyDescription"
    ]
    """<p>The text description for this host key.</p>"""
    type: NotRequired["aws_sdk_transfer.types.host_key_type.HostKeyType"]
    """<p>The encryption algorithm that is used for the host key. The <code>Type</code> parameter is specified by using one of the following values:</p> <ul> <li> <p> <code>ssh-rsa</code> </p> </li> <li> <p> <code>ssh-ed25519</code> </p> </li> <li> <p> <code>ecdsa-sha2-nistp256</code> </p> </li> <li> <p> <code>ecdsa-sha2-nistp384</code> </p> </li> <li> <p> <code>ecdsa-sha2-nistp521</code> </p> </li> </ul>"""
    date_imported: NotRequired["aws_sdk_transfer.types.date_imported.DateImported"]
    """<p>The date on which the host key was added to the server.</p>"""
    tags: NotRequired["aws_sdk_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for host keys.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedHostKey) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "host_key_id" in value:
        out["HostKeyId"] = value["host_key_id"]
    if "host_key_fingerprint" in value:
        out["HostKeyFingerprint"] = value["host_key_fingerprint"]
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
    if "tags" in value:
        import aws_sdk_transfer.types.tags

        out["Tags"] = aws_sdk_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedHostKey:
    out: DescribedHostKey = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribedHostKey.arn required")
    if "HostKeyId" in data:
        out["host_key_id"] = data["HostKeyId"]
    if "HostKeyFingerprint" in data:
        out["host_key_fingerprint"] = data["HostKeyFingerprint"]
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
    if "Tags" in data:
        import aws_sdk_transfer.types.tags

        out["tags"] = aws_sdk_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
