"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateKeyValueStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_value_store_comment
    import aws_sdk_cloudfront.types.key_value_store_name
    import aws_sdk_cloudfront.types.string


class UpdateKeyValueStoreRequest(TypedDict):
    name: "aws_sdk_cloudfront.types.key_value_store_name.KeyValueStoreName"
    """<p>The name of the key value store to update.</p>"""
    comment: "aws_sdk_cloudfront.types.key_value_store_comment.KeyValueStoreComment"
    """<p>The comment of the key value store to update.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The key value store to update, if a match occurs.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateKeyValueStoreRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> UpdateKeyValueStoreRequest:
    out: UpdateKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        raise DeserializationError("UpdateKeyValueStoreRequest.comment required")
    return out
