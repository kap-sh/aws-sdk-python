"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetDistributionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetDistributionRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The distribution's ID. If the ID is empty, an empty distribution configuration is returned.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetDistributionRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetDistributionRequest:
    out: GetDistributionRequest = {}  # type: ignore[typeddict-item]
    return out
