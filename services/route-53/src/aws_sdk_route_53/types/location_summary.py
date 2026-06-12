"""Generated from Smithy shape ``com.amazonaws.route53#LocationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.cidr_location_name_default_allowed


class LocationSummary(TypedDict):
    location_name: NotRequired[
        "aws_sdk_route_53.types.cidr_location_name_default_allowed.CidrLocationNameDefaultAllowed"
    ]
    """<p>A string that specifies a location name.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: LocationSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "location_name" in value:
        SubElement(el, "LocationName").text = str(value["location_name"])


def deserialize_xml(el: Element) -> LocationSummary:
    out: LocationSummary = {}  # type: ignore[typeddict-item]
    child_location_name = el.find("LocationName")
    if child_location_name is not None:
        out["location_name"] = str(child_location_name.text or "")
    return out
