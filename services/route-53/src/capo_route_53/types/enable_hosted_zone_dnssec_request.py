"""Generated from Smithy shape ``com.amazonaws.route53#EnableHostedZoneDNSSECRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_id


class EnableHostedZoneDNSSECRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>A unique string used to identify a hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: EnableHostedZoneDNSSECRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> EnableHostedZoneDNSSECRequest:
    out: EnableHostedZoneDNSSECRequest = {}  # type: ignore[typeddict-item]
    return out
