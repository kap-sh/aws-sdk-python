"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetKeyGroupConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetKeyGroupConfigRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the key group whose configuration you are getting. To get the identifier, use <code>ListKeyGroups</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetKeyGroupConfigRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetKeyGroupConfigRequest:
    out: GetKeyGroupConfigRequest = {}  # type: ignore[typeddict-item]
    return out
