"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetModelInterfaceRelationshipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id


class DescribeAssetModelInterfaceRelationshipRequest(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>"""
    interface_asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetModelInterfaceRelationshipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAssetModelInterfaceRelationshipRequest:
    out: DescribeAssetModelInterfaceRelationshipRequest = {}  # type: ignore[typeddict-item]
    return out
