"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteAnycastIpListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteAnycastIpListRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the Anycast static IP list.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the Anycast static IP list that you are deleting.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteAnycastIpListRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteAnycastIpListRequest:
    out: DeleteAnycastIpListRequest = {}  # type: ignore[typeddict-item]
    return out
