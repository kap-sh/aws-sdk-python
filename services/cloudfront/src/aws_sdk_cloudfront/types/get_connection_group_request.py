"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetConnectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetConnectionGroupRequest(TypedDict, closed=True):
    identifier: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID, name, or Amazon Resource Name (ARN) of the connection group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetConnectionGroupRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetConnectionGroupRequest:
    out: GetConnectionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
