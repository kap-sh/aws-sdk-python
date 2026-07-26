"""Generated from Smithy shape ``com.amazonaws.route53#DeleteReusableDelegationSetResponse``."""

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement


class DeleteReusableDelegationSetResponse(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteReusableDelegationSetResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteReusableDelegationSetResponse:
    out: DeleteReusableDelegationSetResponse = {}  # type: ignore[typeddict-item]
    return out
