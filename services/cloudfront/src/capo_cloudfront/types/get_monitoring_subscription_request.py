"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetMonitoringSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetMonitoringSubscriptionRequest(TypedDict, closed=True):
    distribution_id: "capo_cloudfront.types.string.string"
    """<p>The ID of the distribution that you are getting metrics information for.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetMonitoringSubscriptionRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetMonitoringSubscriptionRequest:
    out: GetMonitoringSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
