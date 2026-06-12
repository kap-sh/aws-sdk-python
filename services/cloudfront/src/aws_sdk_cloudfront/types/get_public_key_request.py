"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetPublicKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetPublicKeyRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the public key you are getting.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetPublicKeyRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetPublicKeyRequest:
    out: GetPublicKeyRequest = {}  # type: ignore[typeddict-item]
    return out
