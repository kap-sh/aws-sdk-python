"""Generated from Smithy shape ``com.amazonaws.route53#DeleteTrafficPolicyInstanceResponse``."""

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement


class DeleteTrafficPolicyInstanceResponse(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteTrafficPolicyInstanceResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteTrafficPolicyInstanceResponse:
    out: DeleteTrafficPolicyInstanceResponse = {}  # type: ignore[typeddict-item]
    return out
