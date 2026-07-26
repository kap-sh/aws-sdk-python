"""Generated from Smithy shape ``com.amazonaws.route53#CreateTrafficPolicyInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.resource_uri
    import capo_route_53.types.traffic_policy_instance


class CreateTrafficPolicyInstanceResponse(TypedDict, closed=True):
    traffic_policy_instance: (
        "capo_route_53.types.traffic_policy_instance.TrafficPolicyInstance"
    )
    """<p>A complex type that contains settings for the new traffic policy instance.</p>"""
    location: "capo_route_53.types.resource_uri.ResourceURI"
    """<p>A unique URL that represents a new traffic policy instance.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateTrafficPolicyInstanceResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.traffic_policy_instance

    capo_route_53.types.traffic_policy_instance.serialize_xml(
        value["traffic_policy_instance"], el, "TrafficPolicyInstance"
    )


def deserialize_xml(el: Element) -> CreateTrafficPolicyInstanceResponse:
    out: CreateTrafficPolicyInstanceResponse = {}  # type: ignore[typeddict-item]
    child_traffic_policy_instance = el.find("TrafficPolicyInstance")
    if child_traffic_policy_instance is not None:
        import capo_route_53.types.traffic_policy_instance

        out["traffic_policy_instance"] = (
            capo_route_53.types.traffic_policy_instance.deserialize_xml(
                child_traffic_policy_instance
            )
        )
    else:
        raise DeserializationError(
            "CreateTrafficPolicyInstanceResponse.traffic_policy_instance required"
        )
    return out
