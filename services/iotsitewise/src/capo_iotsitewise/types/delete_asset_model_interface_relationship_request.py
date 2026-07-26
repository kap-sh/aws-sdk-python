"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteAssetModelInterfaceRelationshipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.custom_id


class DeleteAssetModelInterfaceRelationshipRequest(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>"""
    interface_asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetModelInterfaceRelationshipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssetModelInterfaceRelationshipRequest:
    out: DeleteAssetModelInterfaceRelationshipRequest = {}  # type: ignore[typeddict-item]
    return out
