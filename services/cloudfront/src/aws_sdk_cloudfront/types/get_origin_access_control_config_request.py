"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetOriginAccessControlConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetOriginAccessControlConfigRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The unique identifier of the origin access control.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetOriginAccessControlConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetOriginAccessControlConfigRequest:
    out: GetOriginAccessControlConfigRequest = {}  # type: ignore[typeddict-item]
    return out
