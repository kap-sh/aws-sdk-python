"""Generated from Smithy shape ``com.amazonaws.transfer#ImportHostKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.host_key
    import aws_sdk_transfer.types.host_key_description
    import aws_sdk_transfer.types.server_id
    import aws_sdk_transfer.types.tags


class ImportHostKeyRequest(TypedDict):
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>The identifier of the server that contains the host key that you are importing.</p>"""
    host_key_body: "aws_sdk_transfer.types.host_key.HostKey"
    """<p>The private key portion of an SSH key pair.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p>"""
    description: NotRequired[
        "aws_sdk_transfer.types.host_key_description.HostKeyDescription"
    ]
    """<p>The text description that identifies this host key.</p>"""
    tags: NotRequired["aws_sdk_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for host keys.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportHostKeyRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["HostKeyBody"] = value["host_key_body"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_transfer.types.tags

        out["Tags"] = aws_sdk_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportHostKeyRequest:
    out: ImportHostKeyRequest = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ImportHostKeyRequest.server_id required")
    if "HostKeyBody" in data:
        out["host_key_body"] = data["HostKeyBody"]
    else:
        raise DeserializationError("ImportHostKeyRequest.host_key_body required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_transfer.types.tags

        out["tags"] = aws_sdk_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
