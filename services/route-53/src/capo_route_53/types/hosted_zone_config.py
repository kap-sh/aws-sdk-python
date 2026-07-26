"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.is_private_zone
    import capo_route_53.types.resource_description


class HostedZoneConfig(TypedDict, closed=True):
    comment: NotRequired["capo_route_53.types.resource_description.ResourceDescription"]
    """<p>Any comments that you want to include about the hosted zone.</p>"""
    private_zone: "capo_route_53.types.is_private_zone.IsPrivateZone"
    """<p>A value that indicates whether this is a private hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HostedZoneConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    SubElement(el, "PrivateZone").text = (
        "true" if value.get("private_zone", False) else "false"
    )


def deserialize_xml(el: Element) -> HostedZoneConfig:
    out: HostedZoneConfig = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_private_zone = el.find("PrivateZone")
    if child_private_zone is not None:
        out["private_zone"] = (child_private_zone.text or "").lower() == "true"
    else:
        out["private_zone"] = False
    return out
