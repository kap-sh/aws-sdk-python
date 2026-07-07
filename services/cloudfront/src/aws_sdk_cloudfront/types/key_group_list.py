"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyGroupList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.key_group_summary_list
    import aws_sdk_cloudfront.types.string


class KeyGroupList(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the <code>Marker</code> field of a subsequent request to continue listing key groups.</p>"""
    max_items: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The maximum number of key groups requested.</p>"""
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of key groups returned in the response.</p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.key_group_summary_list.KeyGroupSummaryList"
    ]
    """<p>A list of key groups.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KeyGroupList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    SubElement(el, "MaxItems").text = str(value["max_items"])
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.key_group_summary_list

        aws_sdk_cloudfront.types.key_group_summary_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> KeyGroupList:
    out: KeyGroupList = {}  # type: ignore[typeddict-item]
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        raise DeserializationError("KeyGroupList.max_items required")
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("KeyGroupList.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.key_group_summary_list

        out["items"] = aws_sdk_cloudfront.types.key_group_summary_list.deserialize_xml(
            child_items
        )
    return out
