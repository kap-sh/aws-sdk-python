"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateAssetModelCompositeModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_composite_model_path
    import capo_iotsitewise.types.asset_model_status


class UpdateAssetModelCompositeModelResponse(TypedDict, closed=True):
    asset_model_composite_model_path: "capo_iotsitewise.types.asset_model_composite_model_path.AssetModelCompositeModelPath"
    """<p>The path to the composite model listing the parent composite models.</p>"""
    asset_model_status: "capo_iotsitewise.types.asset_model_status.AssetModelStatus"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetModelCompositeModelResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_model_composite_model_path

    out["assetModelCompositeModelPath"] = (
        capo_iotsitewise.types.asset_model_composite_model_path.serialize_json(
            value["asset_model_composite_model_path"]
        )
    )
    import capo_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = capo_iotsitewise.types.asset_model_status.serialize_json(
        value["asset_model_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAssetModelCompositeModelResponse:
    out: UpdateAssetModelCompositeModelResponse = {}  # type: ignore[typeddict-item]
    if "assetModelCompositeModelPath" in data:
        import capo_iotsitewise.types.asset_model_composite_model_path

        out["asset_model_composite_model_path"] = (
            capo_iotsitewise.types.asset_model_composite_model_path.deserialize_json(
                data["assetModelCompositeModelPath"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssetModelCompositeModelResponse.asset_model_composite_model_path required"
        )
    if "assetModelStatus" in data:
        import capo_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            capo_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssetModelCompositeModelResponse.asset_model_status required"
        )
    return out
