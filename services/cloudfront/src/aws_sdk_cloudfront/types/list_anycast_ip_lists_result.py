"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListAnycastIpListsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.anycast_ip_list_collection


class ListAnycastIpListsResult(TypedDict):
    anycast_ip_lists: NotRequired[
        "aws_sdk_cloudfront.types.anycast_ip_list_collection.AnycastIpListCollection"
    ]
    """<p>Root level tag for the <code>AnycastIpLists</code> parameters.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListAnycastIpListsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "anycast_ip_lists" in value:
        import aws_sdk_cloudfront.types.anycast_ip_list_collection

        aws_sdk_cloudfront.types.anycast_ip_list_collection.serialize_xml(
            value["anycast_ip_lists"], el, "AnycastIpListCollection"
        )


def deserialize_xml(el: Element) -> ListAnycastIpListsResult:
    out: ListAnycastIpListsResult = {}  # type: ignore[typeddict-item]
    child_anycast_ip_lists = el.find("AnycastIpListCollection")
    if child_anycast_ip_lists is not None:
        import aws_sdk_cloudfront.types.anycast_ip_list_collection

        out["anycast_ip_lists"] = (
            aws_sdk_cloudfront.types.anycast_ip_list_collection.deserialize_xml(
                child_anycast_ip_lists
            )
        )
    return out
