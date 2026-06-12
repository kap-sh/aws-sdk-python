"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetCloudFrontOriginAccessIdentityConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetCloudFrontOriginAccessIdentityConfigRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identity's ID.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetCloudFrontOriginAccessIdentityConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetCloudFrontOriginAccessIdentityConfigRequest:
    out: GetCloudFrontOriginAccessIdentityConfigRequest = {}  # type: ignore[typeddict-item]
    return out
