"""Generated from Smithy shape ``com.amazonaws.route53#GetReusableDelegationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_id


class GetReusableDelegationSetRequest(TypedDict, closed=True):
    id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the reusable delegation set that you want to get a list of name servers for.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetReusableDelegationSetRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetReusableDelegationSetRequest:
    out: GetReusableDelegationSetRequest = {}  # type: ignore[typeddict-item]
    return out
