"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListConnectionGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.connection_group_association_filter
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class ListConnectionGroupsRequest(TypedDict, closed=True):
    association_filter: NotRequired[
        "capo_cloudfront.types.connection_group_association_filter.ConnectionGroupAssociationFilter"
    ]
    """<p>Filter by associated Anycast IP list ID.</p>"""
    marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The marker for the next set of connection groups to retrieve.</p>"""
    max_items: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The maximum number of connection groups to return.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListConnectionGroupsRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "association_filter" in value:
        import capo_cloudfront.types.connection_group_association_filter

        capo_cloudfront.types.connection_group_association_filter.serialize_xml(
            value["association_filter"], el, "AssociationFilter"
        )
    if "marker" in value:
        SubElement(el, "Marker").text = str(value["marker"])
    if "max_items" in value:
        SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListConnectionGroupsRequest:
    out: ListConnectionGroupsRequest = {}  # type: ignore[typeddict-item]
    child_association_filter = el.find("AssociationFilter")
    if child_association_filter is not None:
        import capo_cloudfront.types.connection_group_association_filter

        out["association_filter"] = (
            capo_cloudfront.types.connection_group_association_filter.deserialize_xml(
                child_association_filter
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
