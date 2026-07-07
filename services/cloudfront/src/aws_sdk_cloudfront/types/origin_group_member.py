"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginGroupMember``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class OriginGroupMember(TypedDict, closed=True):
    origin_id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID for an origin in an origin group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginGroupMember, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "OriginId").text = str(value["origin_id"])


def deserialize_xml(el: Element) -> OriginGroupMember:
    out: OriginGroupMember = {}  # type: ignore[typeddict-item]
    child_origin_id = el.find("OriginId")
    if child_origin_id is not None:
        out["origin_id"] = str(child_origin_id.text or "")
    else:
        raise DeserializationError("OriginGroupMember.origin_id required")
    return out
