"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateAnycastIpListResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.anycast_ip_list
    import capo_cloudfront.types.string


class CreateAnycastIpListResult(TypedDict, closed=True):
    anycast_ip_list: NotRequired["capo_cloudfront.types.anycast_ip_list.AnycastIpList"]
    """<p>A response structure that includes the version identifier (ETag) and the created <a>AnycastIpList</a> structure.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the Anycast static IP list.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateAnycastIpListResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "anycast_ip_list" in value:
        import capo_cloudfront.types.anycast_ip_list

        capo_cloudfront.types.anycast_ip_list.serialize_xml(
            value["anycast_ip_list"], el, "AnycastIpList"
        )


def deserialize_xml(el: Element) -> CreateAnycastIpListResult:
    out: CreateAnycastIpListResult = {}  # type: ignore[typeddict-item]
    child_anycast_ip_list = el.find("AnycastIpList")
    if child_anycast_ip_list is not None:
        import capo_cloudfront.types.anycast_ip_list

        out["anycast_ip_list"] = capo_cloudfront.types.anycast_ip_list.deserialize_xml(
            child_anycast_ip_list
        )
    return out
