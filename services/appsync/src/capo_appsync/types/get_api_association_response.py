"""Generated from Smithy shape ``com.amazonaws.appsync#GetApiAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.api_association


class GetApiAssociationResponse(TypedDict, closed=True):
    api_association: NotRequired["capo_appsync.types.api_association.ApiAssociation"]
    """<p>The <code>ApiAssociation</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApiAssociationResponse) -> dict:
    out: dict = {}
    if "api_association" in value:
        import capo_appsync.types.api_association

        out["apiAssociation"] = capo_appsync.types.api_association.serialize_json(
            value["api_association"]
        )
    return out


def deserialize_json(data: dict) -> GetApiAssociationResponse:
    out: GetApiAssociationResponse = {}  # type: ignore[typeddict-item]
    if "apiAssociation" in data:
        import capo_appsync.types.api_association

        out["api_association"] = capo_appsync.types.api_association.deserialize_json(
            data["apiAssociation"]
        )
    return out
