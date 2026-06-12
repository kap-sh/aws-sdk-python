"""Generated from Smithy shape ``com.amazonaws.cloudfront#PublicKeySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.timestamp


class PublicKeySummary(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the public key.</p>"""
    name: "aws_sdk_cloudfront.types.string.string"
    """<p>A name to help identify the public key.</p>"""
    created_time: "aws_sdk_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the public key was uploaded.</p>"""
    encoded_key: "aws_sdk_cloudfront.types.string.string"
    """<p>The public key.</p>"""
    comment: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>A comment to describe the public key. The comment cannot be longer than 128 characters.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PublicKeySummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Name").text = str(value["name"])
    import aws_sdk_cloudfront.types.timestamp

    aws_sdk_cloudfront.types.timestamp.serialize_xml(
        value["created_time"], el, "CreatedTime"
    )
    SubElement(el, "EncodedKey").text = str(value["encoded_key"])
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> PublicKeySummary:
    out: PublicKeySummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("PublicKeySummary.id required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("PublicKeySummary.name required")
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import aws_sdk_cloudfront.types.timestamp

        out["created_time"] = aws_sdk_cloudfront.types.timestamp.deserialize_xml(
            child_created_time
        )
    else:
        raise DeserializationError("PublicKeySummary.created_time required")
    child_encoded_key = el.find("EncodedKey")
    if child_encoded_key is not None:
        out["encoded_key"] = str(child_encoded_key.text or "")
    else:
        raise DeserializationError("PublicKeySummary.encoded_key required")
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
