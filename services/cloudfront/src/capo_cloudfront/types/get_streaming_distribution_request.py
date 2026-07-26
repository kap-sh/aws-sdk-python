"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetStreamingDistributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetStreamingDistributionRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The streaming distribution's ID.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetStreamingDistributionRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetStreamingDistributionRequest:
    out: GetStreamingDistributionRequest = {}  # type: ignore[typeddict-item]
    return out
