"""Generated from Smithy shape ``com.amazonaws.s3#Tagging``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.tag_set


class Tagging(TypedDict):
    tag_set: "aws_sdk_s3.types.tag_set.TagSet"
    """<p>A collection for a set of tags</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Tagging, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.tag_set

    aws_sdk_s3.types.tag_set.serialize_xml(value["tag_set"], el, "TagSet")


def deserialize_xml(el: Element) -> Tagging:
    out: Tagging = {}  # type: ignore[typeddict-item]
    child_tag_set = el.find("TagSet")
    if child_tag_set is not None:
        import aws_sdk_s3.types.tag_set

        out["tag_set"] = aws_sdk_s3.types.tag_set.deserialize_xml(child_tag_set)
    else:
        raise DeserializationError("Tagging.tag_set required")
    return out
