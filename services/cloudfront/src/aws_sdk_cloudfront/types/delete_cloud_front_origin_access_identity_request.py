"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteCloudFrontOriginAccessIdentityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteCloudFrontOriginAccessIdentityRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The origin access identity's ID.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header you received from a previous <code>GET</code> or <code>PUT</code> request. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteCloudFrontOriginAccessIdentityRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteCloudFrontOriginAccessIdentityRequest:
    out: DeleteCloudFrontOriginAccessIdentityRequest = {}  # type: ignore[typeddict-item]
    return out
