"""Generated from Smithy shape ``com.amazonaws.route53#GetHealthCheckLastFailureReasonRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.health_check_id


class GetHealthCheckLastFailureReasonRequest(TypedDict, closed=True):
    health_check_id: "aws_sdk_route_53.types.health_check_id.HealthCheckId"
    """<p>The ID for the health check for which you want the last failure reason. When you created the health check, <code>CreateHealthCheck</code> returned the ID in the response, in the <code>HealthCheckId</code> element.</p> <note> <p>If you want to get the last failure reason for a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can't use <code>GetHealthCheckLastFailureReason</code> for a calculated health check.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetHealthCheckLastFailureReasonRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetHealthCheckLastFailureReasonRequest:
    out: GetHealthCheckLastFailureReasonRequest = {}  # type: ignore[typeddict-item]
    return out
