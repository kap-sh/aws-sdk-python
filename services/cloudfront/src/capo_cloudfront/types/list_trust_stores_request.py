"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListTrustStoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class ListTrustStoresRequest(TypedDict, closed=True):
    marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The maximum number of trust stores that you want returned in the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListTrustStoresRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "marker" in value:
        SubElement(el, "Marker").text = str(value["marker"])
    if "max_items" in value:
        SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListTrustStoresRequest:
    out: ListTrustStoresRequest = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
