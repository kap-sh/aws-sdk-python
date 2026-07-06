"""Generated from Smithy shape ``com.amazonaws.route53#DeleteHealthCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.health_check_id


class DeleteHealthCheckRequest(TypedDict, closed=True):
    health_check_id: "aws_sdk_route_53.types.health_check_id.HealthCheckId"
    """<p>The ID of the health check that you want to delete.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteHealthCheckRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteHealthCheckRequest:
    out: DeleteHealthCheckRequest = {}  # type: ignore[typeddict-item]
    return out
