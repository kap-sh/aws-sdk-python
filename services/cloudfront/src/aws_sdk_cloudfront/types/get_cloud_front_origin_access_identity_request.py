"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetCloudFrontOriginAccessIdentityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetCloudFrontOriginAccessIdentityRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identity's ID.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetCloudFrontOriginAccessIdentityRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetCloudFrontOriginAccessIdentityRequest:
    out: GetCloudFrontOriginAccessIdentityRequest = {}  # type: ignore[typeddict-item]
    return out
