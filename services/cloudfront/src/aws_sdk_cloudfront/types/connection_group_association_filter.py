"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConnectionGroupAssociationFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class ConnectionGroupAssociationFilter(TypedDict):
    anycast_ip_list_id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The ID of the Anycast static IP list.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ConnectionGroupAssociationFilter, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "anycast_ip_list_id" in value:
        SubElement(el, "AnycastIpListId").text = str(value["anycast_ip_list_id"])


def deserialize_xml(el: Element) -> ConnectionGroupAssociationFilter:
    out: ConnectionGroupAssociationFilter = {}  # type: ignore[typeddict-item]
    child_anycast_ip_list_id = el.find("AnycastIpListId")
    if child_anycast_ip_list_id is not None:
        out["anycast_ip_list_id"] = str(child_anycast_ip_list_id.text or "")
    return out
