"""Generated from Smithy shape ``com.amazonaws.route53#CidrBlockSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.cidr
    import aws_sdk_route_53.types.cidr_location_name_default_not_allowed


class CidrBlockSummary(TypedDict):
    cidr_block: NotRequired["aws_sdk_route_53.types.cidr.Cidr"]
    """<p>Value for the CIDR block.</p>"""
    location_name: NotRequired[
        "aws_sdk_route_53.types.cidr_location_name_default_not_allowed.CidrLocationNameDefaultNotAllowed"
    ]
    """<p>The location name of the CIDR block.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CidrBlockSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "cidr_block" in value:
        SubElement(el, "CidrBlock").text = str(value["cidr_block"])
    if "location_name" in value:
        SubElement(el, "LocationName").text = str(value["location_name"])


def deserialize_xml(el: Element) -> CidrBlockSummary:
    out: CidrBlockSummary = {}  # type: ignore[typeddict-item]
    child_cidr_block = el.find("CidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    child_location_name = el.find("LocationName")
    if child_location_name is not None:
        out["location_name"] = str(child_location_name.text or "")
    return out
