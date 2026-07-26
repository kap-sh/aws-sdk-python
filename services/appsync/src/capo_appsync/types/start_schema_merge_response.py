"""Generated from Smithy shape ``com.amazonaws.appsync#StartSchemaMergeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.source_api_association_status


class StartSchemaMergeResponse(TypedDict, closed=True):
    source_api_association_status: NotRequired[
        "capo_appsync.types.source_api_association_status.SourceApiAssociationStatus"
    ]
    """<p>The state of the source API association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSchemaMergeResponse) -> dict:
    out: dict = {}
    if "source_api_association_status" in value:
        import capo_appsync.types.source_api_association_status

        out["sourceApiAssociationStatus"] = (
            capo_appsync.types.source_api_association_status.serialize_json(
                value["source_api_association_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartSchemaMergeResponse:
    out: StartSchemaMergeResponse = {}  # type: ignore[typeddict-item]
    if "sourceApiAssociationStatus" in data:
        import capo_appsync.types.source_api_association_status

        out["source_api_association_status"] = (
            capo_appsync.types.source_api_association_status.deserialize_json(
                data["sourceApiAssociationStatus"]
            )
        )
    return out
