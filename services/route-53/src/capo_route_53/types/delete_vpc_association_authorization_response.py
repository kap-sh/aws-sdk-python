"""Generated from Smithy shape ``com.amazonaws.route53#DeleteVPCAssociationAuthorizationResponse``."""

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement


class DeleteVPCAssociationAuthorizationResponse(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteVPCAssociationAuthorizationResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteVPCAssociationAuthorizationResponse:
    out: DeleteVPCAssociationAuthorizationResponse = {}  # type: ignore[typeddict-item]
    return out
