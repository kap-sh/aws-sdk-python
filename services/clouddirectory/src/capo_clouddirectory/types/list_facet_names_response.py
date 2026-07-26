"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListFacetNamesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.facet_name_list
    import capo_clouddirectory.types.next_token


class ListFacetNamesResponse(TypedDict, closed=True):
    facet_names: NotRequired["capo_clouddirectory.types.facet_name_list.FacetNameList"]
    """<p>The names of facets that exist within the schema.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFacetNamesResponse) -> dict:
    out: dict = {}
    if "facet_names" in value:
        import capo_clouddirectory.types.facet_name_list

        out["FacetNames"] = capo_clouddirectory.types.facet_name_list.serialize_json(
            value["facet_names"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFacetNamesResponse:
    out: ListFacetNamesResponse = {}  # type: ignore[typeddict-item]
    if "FacetNames" in data:
        import capo_clouddirectory.types.facet_name_list

        out["facet_names"] = capo_clouddirectory.types.facet_name_list.deserialize_json(
            data["FacetNames"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
