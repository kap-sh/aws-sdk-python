"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListFacetAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.facet_attribute_list
    import capo_clouddirectory.types.next_token


class ListFacetAttributesResponse(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_clouddirectory.types.facet_attribute_list.FacetAttributeList"
    ]
    """<p>The attributes attached to the facet.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFacetAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_clouddirectory.types.facet_attribute_list

        out["Attributes"] = (
            capo_clouddirectory.types.facet_attribute_list.serialize_json(
                value["attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFacetAttributesResponse:
    out: ListFacetAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import capo_clouddirectory.types.facet_attribute_list

        out["attributes"] = (
            capo_clouddirectory.types.facet_attribute_list.deserialize_json(
                data["Attributes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
