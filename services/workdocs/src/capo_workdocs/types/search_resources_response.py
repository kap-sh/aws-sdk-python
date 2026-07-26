"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.next_marker_type
    import capo_workdocs.types.response_items_list


class SearchResourcesResponse(TypedDict, closed=True):
    items: NotRequired["capo_workdocs.types.response_items_list.ResponseItemsList"]
    """<p>List of Documents, Folders, Comments, and Document Versions matching the query.</p>"""
    marker: NotRequired["capo_workdocs.types.next_marker_type.NextMarkerType"]
    """<p>The marker to use when requesting the next set of results. If there are no additional results, the string is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_workdocs.types.response_items_list

        out["Items"] = capo_workdocs.types.response_items_list.serialize_json(
            value["items"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> SearchResourcesResponse:
    out: SearchResourcesResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_workdocs.types.response_items_list

        out["items"] = capo_workdocs.types.response_items_list.deserialize_json(
            data["Items"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
