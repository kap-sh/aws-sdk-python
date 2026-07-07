"""Generated from Smithy shape ``com.amazonaws.route53#GetTrafficPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.traffic_policy


class GetTrafficPolicyResponse(TypedDict, closed=True):
    traffic_policy: "aws_sdk_route_53.types.traffic_policy.TrafficPolicy"
    """<p>A complex type that contains settings for the specified traffic policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetTrafficPolicyResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.traffic_policy

    aws_sdk_route_53.types.traffic_policy.serialize_xml(
        value["traffic_policy"], el, "TrafficPolicy"
    )


def deserialize_xml(el: Element) -> GetTrafficPolicyResponse:
    out: GetTrafficPolicyResponse = {}  # type: ignore[typeddict-item]
    child_traffic_policy = el.find("TrafficPolicy")
    if child_traffic_policy is not None:
        import aws_sdk_route_53.types.traffic_policy

        out["traffic_policy"] = aws_sdk_route_53.types.traffic_policy.deserialize_xml(
            child_traffic_policy
        )
    else:
        raise DeserializationError("GetTrafficPolicyResponse.traffic_policy required")
    return out
