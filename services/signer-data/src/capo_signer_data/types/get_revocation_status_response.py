"""Generated from Smithy shape ``com.amazonaws.signerdata#GetRevocationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer_data.types.revoked_entities


class GetRevocationStatusResponse(TypedDict, closed=True):
    revoked_entities: NotRequired[
        "capo_signer_data.types.revoked_entities.RevokedEntities"
    ]
    """<p>List of entity identifiers that have been revoked. Empty if no revocations found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRevocationStatusResponse) -> dict:
    out: dict = {}
    if "revoked_entities" in value:
        import capo_signer_data.types.revoked_entities

        out["revokedEntities"] = capo_signer_data.types.revoked_entities.serialize_json(
            value["revoked_entities"]
        )
    return out


def deserialize_json(data: dict) -> GetRevocationStatusResponse:
    out: GetRevocationStatusResponse = {}  # type: ignore[typeddict-item]
    if "revokedEntities" in data:
        import capo_signer_data.types.revoked_entities

        out["revoked_entities"] = (
            capo_signer_data.types.revoked_entities.deserialize_json(
                data["revokedEntities"]
            )
        )
    return out
