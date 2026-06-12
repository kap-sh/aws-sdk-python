"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetInvalidationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetInvalidationRequest(TypedDict):
    distribution_id: "aws_sdk_cloudfront.types.string.string"
    """<p>The distribution's ID.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier for the invalidation request, for example, <code>IDFDVBD632BHDS5</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetInvalidationRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetInvalidationRequest:
    out: GetInvalidationRequest = {}  # type: ignore[typeddict-item]
    return out
