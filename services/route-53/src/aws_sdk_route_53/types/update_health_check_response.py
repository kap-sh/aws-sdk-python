"""Generated from Smithy shape ``com.amazonaws.route53#UpdateHealthCheckResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.health_check


class UpdateHealthCheckResponse(TypedDict):
    health_check: "aws_sdk_route_53.types.health_check.HealthCheck"
    """<p>A complex type that contains the response to an <code>UpdateHealthCheck</code> request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateHealthCheckResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.health_check

    aws_sdk_route_53.types.health_check.serialize_xml(
        value["health_check"], el, "HealthCheck"
    )


def deserialize_xml(el: Element) -> UpdateHealthCheckResponse:
    out: UpdateHealthCheckResponse = {}  # type: ignore[typeddict-item]
    child_health_check = el.find("HealthCheck")
    if child_health_check is not None:
        import aws_sdk_route_53.types.health_check

        out["health_check"] = aws_sdk_route_53.types.health_check.deserialize_xml(
            child_health_check
        )
    else:
        raise DeserializationError("UpdateHealthCheckResponse.health_check required")
    return out
