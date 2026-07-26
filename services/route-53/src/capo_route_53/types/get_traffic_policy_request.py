"""Generated from Smithy shape ``com.amazonaws.route53#GetTrafficPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.traffic_policy_id
    import capo_route_53.types.traffic_policy_version


class GetTrafficPolicyRequest(TypedDict, closed=True):
    id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>The ID of the traffic policy that you want to get information about.</p>"""
    version: "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion"
    """<p>The version number of the traffic policy that you want to get information about.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetTrafficPolicyRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetTrafficPolicyRequest:
    out: GetTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
