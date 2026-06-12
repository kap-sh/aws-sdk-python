"""Generated from Smithy shape ``com.amazonaws.route53#UpdateTrafficPolicyInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.traffic_policy_instance


class UpdateTrafficPolicyInstanceResponse(TypedDict):
    traffic_policy_instance: (
        "aws_sdk_route_53.types.traffic_policy_instance.TrafficPolicyInstance"
    )
    """<p>A complex type that contains settings for the updated traffic policy instance.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateTrafficPolicyInstanceResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.traffic_policy_instance

    aws_sdk_route_53.types.traffic_policy_instance.serialize_xml(
        value["traffic_policy_instance"], el, "TrafficPolicyInstance"
    )


def deserialize_xml(el: Element) -> UpdateTrafficPolicyInstanceResponse:
    out: UpdateTrafficPolicyInstanceResponse = {}  # type: ignore[typeddict-item]
    child_traffic_policy_instance = el.find("TrafficPolicyInstance")
    if child_traffic_policy_instance is not None:
        import aws_sdk_route_53.types.traffic_policy_instance

        out["traffic_policy_instance"] = (
            aws_sdk_route_53.types.traffic_policy_instance.deserialize_xml(
                child_traffic_policy_instance
            )
        )
    else:
        raise DeserializationError(
            "UpdateTrafficPolicyInstanceResponse.traffic_policy_instance required"
        )
    return out
