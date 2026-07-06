"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetFacetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.facet


class GetFacetResponse(TypedDict, closed=True):
    facet: NotRequired["aws_sdk_clouddirectory.types.facet.Facet"]
    """<p>The <a>Facet</a> structure that is associated with the facet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFacetResponse) -> dict:
    out: dict = {}
    if "facet" in value:
        import aws_sdk_clouddirectory.types.facet

        out["Facet"] = aws_sdk_clouddirectory.types.facet.serialize_json(value["facet"])
    return out


def deserialize_json(data: dict) -> GetFacetResponse:
    out: GetFacetResponse = {}  # type: ignore[typeddict-item]
    if "Facet" in data:
        import aws_sdk_clouddirectory.types.facet

        out["facet"] = aws_sdk_clouddirectory.types.facet.deserialize_json(
            data["Facet"]
        )
    return out
