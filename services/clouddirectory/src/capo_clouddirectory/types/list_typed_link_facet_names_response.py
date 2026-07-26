"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListTypedLinkFacetNamesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.typed_link_name_list


class ListTypedLinkFacetNamesResponse(TypedDict, closed=True):
    facet_names: NotRequired[
        "capo_clouddirectory.types.typed_link_name_list.TypedLinkNameList"
    ]
    """<p>The names of typed link facets that exist within the schema.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTypedLinkFacetNamesResponse) -> dict:
    out: dict = {}
    if "facet_names" in value:
        import capo_clouddirectory.types.typed_link_name_list

        out["FacetNames"] = (
            capo_clouddirectory.types.typed_link_name_list.serialize_json(
                value["facet_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTypedLinkFacetNamesResponse:
    out: ListTypedLinkFacetNamesResponse = {}  # type: ignore[typeddict-item]
    if "FacetNames" in data:
        import capo_clouddirectory.types.typed_link_name_list

        out["facet_names"] = (
            capo_clouddirectory.types.typed_link_name_list.deserialize_json(
                data["FacetNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
