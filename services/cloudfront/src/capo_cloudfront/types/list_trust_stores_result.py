"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListTrustStoresResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string
    import capo_cloudfront.types.trust_store_list


class ListTrustStoresResult(TypedDict, closed=True):
    next_marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>Indicates the next page of trust stores. To get the next page of the list, use this value in the <code>Marker</code> field of your request.</p>"""
    trust_store_list: NotRequired[
        "capo_cloudfront.types.trust_store_list.TrustStoreList"
    ]
    """<p>The trust store list.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListTrustStoresResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    if "trust_store_list" in value:
        import capo_cloudfront.types.trust_store_list

        capo_cloudfront.types.trust_store_list.serialize_xml(
            value["trust_store_list"], el, "TrustStoreList"
        )


def deserialize_xml(el: Element) -> ListTrustStoresResult:
    out: ListTrustStoresResult = {}  # type: ignore[typeddict-item]
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_trust_store_list = el.find("TrustStoreList")
    if child_trust_store_list is not None:
        import capo_cloudfront.types.trust_store_list

        out["trust_store_list"] = (
            capo_cloudfront.types.trust_store_list.deserialize_xml(
                child_trust_store_list
            )
        )
    return out
