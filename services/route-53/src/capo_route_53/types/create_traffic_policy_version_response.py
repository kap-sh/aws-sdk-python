"""Generated from Smithy shape ``com.amazonaws.route53#CreateTrafficPolicyVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.resource_uri
    import capo_route_53.types.traffic_policy


class CreateTrafficPolicyVersionResponse(TypedDict, closed=True):
    traffic_policy: "capo_route_53.types.traffic_policy.TrafficPolicy"
    """<p>A complex type that contains settings for the new version of the traffic policy.</p>"""
    location: "capo_route_53.types.resource_uri.ResourceURI"
    """<p>A unique URL that represents a new traffic policy version.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateTrafficPolicyVersionResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.traffic_policy

    capo_route_53.types.traffic_policy.serialize_xml(
        value["traffic_policy"], el, "TrafficPolicy"
    )


def deserialize_xml(el: Element) -> CreateTrafficPolicyVersionResponse:
    out: CreateTrafficPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    child_traffic_policy = el.find("TrafficPolicy")
    if child_traffic_policy is not None:
        import capo_route_53.types.traffic_policy

        out["traffic_policy"] = capo_route_53.types.traffic_policy.deserialize_xml(
            child_traffic_policy
        )
    else:
        raise DeserializationError(
            "CreateTrafficPolicyVersionResponse.traffic_policy required"
        )
    return out
