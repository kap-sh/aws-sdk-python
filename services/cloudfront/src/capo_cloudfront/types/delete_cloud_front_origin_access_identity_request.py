"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteCloudFrontOriginAccessIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class DeleteCloudFrontOriginAccessIdentityRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The origin access identity's ID.</p>"""
    if_match: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header you received from a previous <code>GET</code> or <code>PUT</code> request. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteCloudFrontOriginAccessIdentityRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteCloudFrontOriginAccessIdentityRequest:
    out: DeleteCloudFrontOriginAccessIdentityRequest = {}  # type: ignore[typeddict-item]
    return out
