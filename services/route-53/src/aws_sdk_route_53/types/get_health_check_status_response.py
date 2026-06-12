"""Generated from Smithy shape ``com.amazonaws.route53#GetHealthCheckStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.health_check_observations


class GetHealthCheckStatusResponse(TypedDict):
    health_check_observations: (
        "aws_sdk_route_53.types.health_check_observations.HealthCheckObservations"
    )
    """<p>A list that contains one <code>HealthCheckObservation</code> element for each Amazon Route 53 health checker that is reporting a status about the health check endpoint.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetHealthCheckStatusResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.health_check_observations

    aws_sdk_route_53.types.health_check_observations.serialize_xml(
        value["health_check_observations"], el, "HealthCheckObservations"
    )


def deserialize_xml(el: Element) -> GetHealthCheckStatusResponse:
    out: GetHealthCheckStatusResponse = {}  # type: ignore[typeddict-item]
    child_health_check_observations = el.find("HealthCheckObservations")
    if child_health_check_observations is not None:
        import aws_sdk_route_53.types.health_check_observations

        out["health_check_observations"] = (
            aws_sdk_route_53.types.health_check_observations.deserialize_xml(
                child_health_check_observations
            )
        )
    else:
        raise DeserializationError(
            "GetHealthCheckStatusResponse.health_check_observations required"
        )
    return out
