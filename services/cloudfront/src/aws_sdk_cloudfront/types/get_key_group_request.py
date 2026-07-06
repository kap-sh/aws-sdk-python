"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetKeyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetKeyGroupRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the key group that you are getting. To get the identifier, use <code>ListKeyGroups</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetKeyGroupRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetKeyGroupRequest:
    out: GetKeyGroupRequest = {}  # type: ignore[typeddict-item]
    return out
