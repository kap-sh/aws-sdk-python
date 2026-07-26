"""Generated from Smithy shape ``com.amazonaws.qapps#ListLibraryItemsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.library_item_list


class ListLibraryItemsOutput(TypedDict, closed=True):
    library_items: NotRequired["capo_qapps.types.library_item_list.LibraryItemList"]
    """<p>The list of library items meeting the request criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLibraryItemsOutput) -> dict:
    out: dict = {}
    if "library_items" in value:
        import capo_qapps.types.library_item_list

        out["libraryItems"] = capo_qapps.types.library_item_list.serialize_json(
            value["library_items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLibraryItemsOutput:
    out: ListLibraryItemsOutput = {}  # type: ignore[typeddict-item]
    if "libraryItems" in data:
        import capo_qapps.types.library_item_list

        out["library_items"] = capo_qapps.types.library_item_list.deserialize_json(
            data["libraryItems"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
