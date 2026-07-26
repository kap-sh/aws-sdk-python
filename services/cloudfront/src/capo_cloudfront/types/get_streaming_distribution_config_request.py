"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetStreamingDistributionConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetStreamingDistributionConfigRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The streaming distribution's ID.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetStreamingDistributionConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetStreamingDistributionConfigRequest:
    out: GetStreamingDistributionConfigRequest = {}  # type: ignore[typeddict-item]
    return out
