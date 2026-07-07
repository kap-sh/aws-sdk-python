"""Generated from Smithy shape ``com.amazonaws.route53#GetTrafficPolicyInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.traffic_policy_instance_id


class GetTrafficPolicyInstanceRequest(TypedDict, closed=True):
    id: "aws_sdk_route_53.types.traffic_policy_instance_id.TrafficPolicyInstanceId"
    """<p>The ID of the traffic policy instance that you want to get information about.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetTrafficPolicyInstanceRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetTrafficPolicyInstanceRequest:
    out: GetTrafficPolicyInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
