"""Generated from Smithy shape ``com.amazonaws.appsync#GetSourceApiAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.source_api_association


class GetSourceApiAssociationResponse(TypedDict, closed=True):
    source_api_association: NotRequired[
        "capo_appsync.types.source_api_association.SourceApiAssociation"
    ]
    """<p>The <code>SourceApiAssociation</code> object data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSourceApiAssociationResponse) -> dict:
    out: dict = {}
    if "source_api_association" in value:
        import capo_appsync.types.source_api_association

        out["sourceApiAssociation"] = (
            capo_appsync.types.source_api_association.serialize_json(
                value["source_api_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSourceApiAssociationResponse:
    out: GetSourceApiAssociationResponse = {}  # type: ignore[typeddict-item]
    if "sourceApiAssociation" in data:
        import capo_appsync.types.source_api_association

        out["source_api_association"] = (
            capo_appsync.types.source_api_association.deserialize_json(
                data["sourceApiAssociation"]
            )
        )
    return out
