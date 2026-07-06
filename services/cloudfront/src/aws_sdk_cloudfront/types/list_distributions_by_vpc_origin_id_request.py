"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionsByVpcOriginIdRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListDistributionsByVpcOriginIdRequest(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The marker associated with the VPC origin distributions list.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of items included in the list.</p>"""
    vpc_origin_id: "aws_sdk_cloudfront.types.string.string"
    """<p>The VPC origin ID.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionsByVpcOriginIdRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListDistributionsByVpcOriginIdRequest:
    out: ListDistributionsByVpcOriginIdRequest = {}  # type: ignore[typeddict-item]
    return out
