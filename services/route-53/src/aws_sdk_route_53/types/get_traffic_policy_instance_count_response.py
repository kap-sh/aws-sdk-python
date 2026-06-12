"""Generated from Smithy shape ``com.amazonaws.route53#GetTrafficPolicyInstanceCountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.traffic_policy_instance_count


class GetTrafficPolicyInstanceCountResponse(TypedDict):
    traffic_policy_instance_count: "aws_sdk_route_53.types.traffic_policy_instance_count.TrafficPolicyInstanceCount"
    """<p>The number of traffic policy instances that are associated with the current Amazon Web Services account.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetTrafficPolicyInstanceCountResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "TrafficPolicyInstanceCount").text = str(
        value["traffic_policy_instance_count"]
    )


def deserialize_xml(el: Element) -> GetTrafficPolicyInstanceCountResponse:
    out: GetTrafficPolicyInstanceCountResponse = {}  # type: ignore[typeddict-item]
    child_traffic_policy_instance_count = el.find("TrafficPolicyInstanceCount")
    if child_traffic_policy_instance_count is not None:
        out["traffic_policy_instance_count"] = int(
            child_traffic_policy_instance_count.text or ""
        )
    else:
        raise DeserializationError(
            "GetTrafficPolicyInstanceCountResponse.traffic_policy_instance_count required"
        )
    return out
