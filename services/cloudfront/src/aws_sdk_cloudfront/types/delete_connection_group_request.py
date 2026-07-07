"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteConnectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteConnectionGroupRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the connection group to delete.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The value of the <code>ETag</code> header that you received when retrieving the connection group to delete.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteConnectionGroupRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteConnectionGroupRequest:
    out: DeleteConnectionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
