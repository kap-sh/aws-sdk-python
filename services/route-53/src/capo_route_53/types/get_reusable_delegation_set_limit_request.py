"""Generated from Smithy shape ``com.amazonaws.route53#GetReusableDelegationSetLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_id
    import capo_route_53.types.reusable_delegation_set_limit_type


class GetReusableDelegationSetLimitRequest(TypedDict, closed=True):
    type: "capo_route_53.types.reusable_delegation_set_limit_type.ReusableDelegationSetLimitType"
    """<p>Specify <code>MAX_ZONES_BY_REUSABLE_DELEGATION_SET</code> to get the maximum number of hosted zones that you can associate with the specified reusable delegation set.</p>"""
    delegation_set_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the delegation set that you want to get the limit for.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetReusableDelegationSetLimitRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetReusableDelegationSetLimitRequest:
    out: GetReusableDelegationSetLimitRequest = {}  # type: ignore[typeddict-item]
    return out
