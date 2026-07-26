"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetCloudFrontOriginAccessIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetCloudFrontOriginAccessIdentityRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identity's ID.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetCloudFrontOriginAccessIdentityRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetCloudFrontOriginAccessIdentityRequest:
    out: GetCloudFrontOriginAccessIdentityRequest = {}  # type: ignore[typeddict-item]
    return out
