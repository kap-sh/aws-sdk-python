"""Generated from Smithy shape ``com.amazonaws.route53#GetTrafficPolicyInstanceCountRequest``."""

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement


class GetTrafficPolicyInstanceCountRequest(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: GetTrafficPolicyInstanceCountRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetTrafficPolicyInstanceCountRequest:
    out: GetTrafficPolicyInstanceCountRequest = {}  # type: ignore[typeddict-item]
    return out
