"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.attachment_hash
    import aws_sdk_ssm.types.attachment_hash_type
    import aws_sdk_ssm.types.attachment_name
    import aws_sdk_ssm.types.attachment_url
    import aws_sdk_ssm.types.content_length


class AttachmentContent(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ssm.types.attachment_name.AttachmentName"]
    """<p>The name of an attachment.</p>"""
    size: "aws_sdk_ssm.types.content_length.ContentLength"
    """<p>The size of an attachment in bytes.</p>"""
    hash: NotRequired["aws_sdk_ssm.types.attachment_hash.AttachmentHash"]
    """<p>The cryptographic hash value of the document content.</p>"""
    hash_type: NotRequired["aws_sdk_ssm.types.attachment_hash_type.AttachmentHashType"]
    """<p>The hash algorithm used to calculate the hash value.</p>"""
    url: NotRequired["aws_sdk_ssm.types.attachment_url.AttachmentUrl"]
    """<p>The URL location of the attachment content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentContent) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["Size"] = value.get("size", 0)
    if "hash" in value:
        out["Hash"] = value["hash"]
    if "hash_type" in value:
        import aws_sdk_ssm.types.attachment_hash_type

        out["HashType"] = aws_sdk_ssm.types.attachment_hash_type.serialize_aws_json_1_1(
            value["hash_type"]
        )
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentContent:
    out: AttachmentContent = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if "Hash" in data:
        out["hash"] = data["Hash"]
    if "HashType" in data:
        import aws_sdk_ssm.types.attachment_hash_type

        out["hash_type"] = (
            aws_sdk_ssm.types.attachment_hash_type.deserialize_aws_json_1_1(
                data["HashType"]
            )
        )
    if "Url" in data:
        out["url"] = data["Url"]
    return out
