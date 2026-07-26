"""Generated from Smithy shape ``com.amazonaws.route53#GetHealthCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.health_check_id


class GetHealthCheckRequest(TypedDict, closed=True):
    health_check_id: "capo_route_53.types.health_check_id.HealthCheckId"
    """<p>The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetHealthCheckRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetHealthCheckRequest:
    out: GetHealthCheckRequest = {}  # type: ignore[typeddict-item]
    return out
