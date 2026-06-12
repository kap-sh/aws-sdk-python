"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteVpcOriginRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteVpcOriginRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The VPC origin ID.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The version identifier of the VPC origin to delete. This is the <code>ETag</code> value returned in the response to <a>GetVpcOrigin</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteVpcOriginRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteVpcOriginRequest:
    out: DeleteVpcOriginRequest = {}  # type: ignore[typeddict-item]
    return out
