"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.attachment_hash
    import capo_ssm.types.attachment_hash_type
    import capo_ssm.types.attachment_name
    import capo_ssm.types.attachment_url
    import capo_ssm.types.content_length


class AttachmentContent(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.attachment_name.AttachmentName"]
    """<p>The name of an attachment.</p>"""
    size: "capo_ssm.types.content_length.ContentLength"
    """<p>The size of an attachment in bytes.</p>"""
    hash: NotRequired["capo_ssm.types.attachment_hash.AttachmentHash"]
    """<p>The cryptographic hash value of the document content.</p>"""
    hash_type: NotRequired["capo_ssm.types.attachment_hash_type.AttachmentHashType"]
    """<p>The hash algorithm used to calculate the hash value.</p>"""
    url: NotRequired["capo_ssm.types.attachment_url.AttachmentUrl"]
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
        import capo_ssm.types.attachment_hash_type

        out["HashType"] = capo_ssm.types.attachment_hash_type.serialize_aws_json_1_1(
            value["hash_type"]
        )
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentContent:
    out: AttachmentContent = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if data.get("Hash") is not None:
        out["hash"] = data["Hash"]
    if data.get("HashType") is not None:
        import capo_ssm.types.attachment_hash_type

        out["hash_type"] = capo_ssm.types.attachment_hash_type.deserialize_aws_json_1_1(
            data["HashType"]
        )
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out
