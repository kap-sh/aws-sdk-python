"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetDistributionConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetDistributionConfigRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The distribution's ID. If the ID is empty, an empty distribution configuration is returned.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetDistributionConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetDistributionConfigRequest:
    out: GetDistributionConfigRequest = {}  # type: ignore[typeddict-item]
    return out
