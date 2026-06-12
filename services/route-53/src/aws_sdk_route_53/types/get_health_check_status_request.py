"""Generated from Smithy shape ``com.amazonaws.route53#GetHealthCheckStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.health_check_id


class GetHealthCheckStatusRequest(TypedDict):
    health_check_id: "aws_sdk_route_53.types.health_check_id.HealthCheckId"
    """<p>The ID for the health check that you want the current status for. When you created the health check, <code>CreateHealthCheck</code> returned the ID in the response, in the <code>HealthCheckId</code> element.</p> <note> <p>If you want to check the status of a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can't use <code>GetHealthCheckStatus</code> to get the status of a calculated health check.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetHealthCheckStatusRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetHealthCheckStatusRequest:
    out: GetHealthCheckStatusRequest = {}  # type: ignore[typeddict-item]
    return out
