"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetStreamingDistributionConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetStreamingDistributionConfigRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The streaming distribution's ID.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetStreamingDistributionConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetStreamingDistributionConfigRequest:
    out: GetStreamingDistributionConfigRequest = {}  # type: ignore[typeddict-item]
    return out
