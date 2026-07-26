"""Generated from Smithy shape ``com.amazonaws.route53#CreateHealthCheckResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.health_check
    import capo_route_53.types.resource_uri


class CreateHealthCheckResponse(TypedDict, closed=True):
    health_check: "capo_route_53.types.health_check.HealthCheck"
    """<p>A complex type that contains identifying information about the health check.</p>"""
    location: "capo_route_53.types.resource_uri.ResourceURI"
    """<p>The unique URL representing the new health check.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateHealthCheckResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.health_check

    capo_route_53.types.health_check.serialize_xml(
        value["health_check"], el, "HealthCheck"
    )


def deserialize_xml(el: Element) -> CreateHealthCheckResponse:
    out: CreateHealthCheckResponse = {}  # type: ignore[typeddict-item]
    child_health_check = el.find("HealthCheck")
    if child_health_check is not None:
        import capo_route_53.types.health_check

        out["health_check"] = capo_route_53.types.health_check.deserialize_xml(
            child_health_check
        )
    else:
        raise DeserializationError("CreateHealthCheckResponse.health_check required")
    return out
