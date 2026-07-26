"""Generated from Smithy shape ``com.amazonaws.route53#VPC``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.vpc_id
    import capo_route_53.types.vpc_region


class VPC(TypedDict, closed=True):
    vpc_region: NotRequired["capo_route_53.types.vpc_region.VPCRegion"]
    """<p>(Private hosted zones only) The region that an Amazon VPC was created in.</p>"""
    vpc_id: NotRequired["capo_route_53.types.vpc_id.VPCId"]


# --- restXml ser/de ---
def serialize_xml(value: VPC, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "vpc_region" in value:
        import capo_route_53.types.vpc_region

        capo_route_53.types.vpc_region.serialize_xml(
            value["vpc_region"], el, "VPCRegion"
        )
    if "vpc_id" in value:
        SubElement(el, "VPCId").text = str(value["vpc_id"])


def deserialize_xml(el: Element) -> VPC:
    out: VPC = {}  # type: ignore[typeddict-item]
    child_vpc_region = el.find("VPCRegion")
    if child_vpc_region is not None:
        import capo_route_53.types.vpc_region

        out["vpc_region"] = capo_route_53.types.vpc_region.deserialize_xml(
            child_vpc_region
        )
    child_vpc_id = el.find("VPCId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
