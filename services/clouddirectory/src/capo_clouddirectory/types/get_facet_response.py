"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetFacetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.facet


class GetFacetResponse(TypedDict, closed=True):
    facet: NotRequired["capo_clouddirectory.types.facet.Facet"]
    """<p>The <a>Facet</a> structure that is associated with the facet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFacetResponse) -> dict:
    out: dict = {}
    if "facet" in value:
        import capo_clouddirectory.types.facet

        out["Facet"] = capo_clouddirectory.types.facet.serialize_json(value["facet"])
    return out


def deserialize_json(data: dict) -> GetFacetResponse:
    out: GetFacetResponse = {}  # type: ignore[typeddict-item]
    if "Facet" in data:
        import capo_clouddirectory.types.facet

        out["facet"] = capo_clouddirectory.types.facet.deserialize_json(data["Facet"])
    return out
