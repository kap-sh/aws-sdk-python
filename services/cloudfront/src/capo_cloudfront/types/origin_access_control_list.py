"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControlList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.origin_access_control_summary_list
    import capo_cloudfront.types.string


class OriginAccessControlList(TypedDict, closed=True):
    marker: "capo_cloudfront.types.string.string"
    """<p>The value of the <code>Marker</code> field that was provided in the request.</p>"""
    next_marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>If there are more items in the list than are in this response, this element is present. It contains the value to use in the <code>Marker</code> field of another request to continue listing origin access controls.</p>"""
    max_items: "capo_cloudfront.types.integer.integer"
    """<p>The maximum number of origin access controls requested.</p>"""
    is_truncated: "capo_cloudfront.types.boolean.boolean"
    """<p>If there are more items in the list than are in this response, this value is <code>true</code>.</p>"""
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of origin access controls returned in the response.</p>"""
    items: NotRequired[
        "capo_cloudfront.types.origin_access_control_summary_list.OriginAccessControlSummaryList"
    ]
    """<p>Contains the origin access controls in the list.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginAccessControlList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Marker").text = str(value["marker"])
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    SubElement(el, "MaxItems").text = str(value["max_items"])
    SubElement(el, "IsTruncated").text = "true" if value["is_truncated"] else "false"
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.origin_access_control_summary_list

        capo_cloudfront.types.origin_access_control_summary_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> OriginAccessControlList:
    out: OriginAccessControlList = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    else:
        raise DeserializationError("OriginAccessControlList.marker required")
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        raise DeserializationError("OriginAccessControlList.max_items required")
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        raise DeserializationError("OriginAccessControlList.is_truncated required")
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("OriginAccessControlList.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.origin_access_control_summary_list

        out["items"] = (
            capo_cloudfront.types.origin_access_control_summary_list.deserialize_xml(
                child_items
            )
        )
    return out
