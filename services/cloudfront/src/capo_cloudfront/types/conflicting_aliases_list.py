"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConflictingAliasesList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.conflicting_aliases
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class ConflictingAliasesList(TypedDict, closed=True):
    next_marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the <code>Marker</code> field of a subsequent request to continue listing conflicting aliases where you left off.</p>"""
    max_items: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The maximum number of conflicting aliases requested.</p>"""
    quantity: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The number of conflicting aliases returned in the response.</p>"""
    items: NotRequired["capo_cloudfront.types.conflicting_aliases.ConflictingAliases"]
    """<p>Contains the conflicting aliases in the list.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ConflictingAliasesList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    if "max_items" in value:
        SubElement(el, "MaxItems").text = str(value["max_items"])
    if "quantity" in value:
        SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.conflicting_aliases

        capo_cloudfront.types.conflicting_aliases.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> ConflictingAliasesList:
    out: ConflictingAliasesList = {}  # type: ignore[typeddict-item]
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.conflicting_aliases

        out["items"] = capo_cloudfront.types.conflicting_aliases.deserialize_xml(
            child_items
        )
    return out
