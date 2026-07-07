"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteMonitoringSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteMonitoringSubscriptionRequest(TypedDict, closed=True):
    distribution_id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the distribution that you are disabling metrics for.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteMonitoringSubscriptionRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteMonitoringSubscriptionRequest:
    out: DeleteMonitoringSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
