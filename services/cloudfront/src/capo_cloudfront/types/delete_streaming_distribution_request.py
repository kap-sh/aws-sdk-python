"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteStreamingDistributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class DeleteStreamingDistributionRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The distribution ID.</p>"""
    if_match: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when you disabled the streaming distribution. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteStreamingDistributionRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteStreamingDistributionRequest:
    out: DeleteStreamingDistributionRequest = {}  # type: ignore[typeddict-item]
    return out
