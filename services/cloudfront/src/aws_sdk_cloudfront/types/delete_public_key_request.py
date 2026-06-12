"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeletePublicKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeletePublicKeyRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the public key you want to remove from CloudFront.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when retrieving the public key identity to delete. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeletePublicKeyRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeletePublicKeyRequest:
    out: DeletePublicKeyRequest = {}  # type: ignore[typeddict-item]
    return out
