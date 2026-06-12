"""Generated from Smithy shape ``com.amazonaws.route53#DeleteTrafficPolicyResponse``."""

from typing import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement


class DeleteTrafficPolicyResponse(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteTrafficPolicyResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteTrafficPolicyResponse:
    out: DeleteTrafficPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
