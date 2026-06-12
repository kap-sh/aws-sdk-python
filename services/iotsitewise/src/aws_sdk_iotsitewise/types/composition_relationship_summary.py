"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CompositionRelationshipSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name


class CompositionRelationshipSummary(TypedDict):
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    asset_model_composite_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of a composite model on this asset model.</p>"""
    asset_model_composite_model_type: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The composite model type. Valid values are <code>AWS/ALARM</code>, <code>CUSTOM</code>, or <code> AWS/L4E_ANOMALY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositionRelationshipSummary) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["assetModelCompositeModelId"] = value["asset_model_composite_model_id"]
    out["assetModelCompositeModelType"] = value["asset_model_composite_model_type"]
    return out


def deserialize_json(data: dict) -> CompositionRelationshipSummary:
    out: CompositionRelationshipSummary = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "CompositionRelationshipSummary.asset_model_id required"
        )
    if "assetModelCompositeModelId" in data:
        out["asset_model_composite_model_id"] = data["assetModelCompositeModelId"]
    else:
        raise DeserializationError(
            "CompositionRelationshipSummary.asset_model_composite_model_id required"
        )
    if "assetModelCompositeModelType" in data:
        out["asset_model_composite_model_type"] = data["assetModelCompositeModelType"]
    else:
        raise DeserializationError(
            "CompositionRelationshipSummary.asset_model_composite_model_type required"
        )
    return out
