"""Generated from Smithy shape ``com.amazonaws.route53#DeleteTrafficPolicyInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.traffic_policy_instance_id


class DeleteTrafficPolicyInstanceRequest(TypedDict):
    id: "aws_sdk_route_53.types.traffic_policy_instance_id.TrafficPolicyInstanceId"
    """<p>The ID of the traffic policy instance that you want to delete. </p> <important> <p>When you delete a traffic policy instance, Amazon Route 53 also deletes all of the resource record sets that were created when you created the traffic policy instance.</p> </important>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteTrafficPolicyInstanceRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteTrafficPolicyInstanceRequest:
    out: DeleteTrafficPolicyInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
