"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyValueStore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.timestamp


class KeyValueStore(TypedDict, closed=True):
    name: "aws_sdk_cloudfront.types.string.string"
    """<p>The name of the key value store.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The unique Id for the key value store.</p>"""
    comment: "aws_sdk_cloudfront.types.string.string"
    """<p>A comment for the key value store.</p>"""
    arn: "aws_sdk_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the key value store.</p>"""
    status: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The status of the key value store.</p>"""
    last_modified_time: "aws_sdk_cloudfront.types.timestamp.timestamp"
    """<p>The last-modified time of the key value store.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KeyValueStore, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Comment").text = str(value["comment"])
    SubElement(el, "ARN").text = str(value["arn"])
    if "status" in value:
        SubElement(el, "Status").text = str(value["status"])
    import aws_sdk_cloudfront.types.timestamp

    aws_sdk_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )


def deserialize_xml(el: Element) -> KeyValueStore:
    out: KeyValueStore = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("KeyValueStore.name required")
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("KeyValueStore.id required")
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        raise DeserializationError("KeyValueStore.comment required")
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("KeyValueStore.arn required")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import aws_sdk_cloudfront.types.timestamp

        out["last_modified_time"] = aws_sdk_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        raise DeserializationError("KeyValueStore.last_modified_time required")
    return out
