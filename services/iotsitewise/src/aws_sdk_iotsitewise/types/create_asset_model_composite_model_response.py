"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateAssetModelCompositeModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_composite_model_path
    import aws_sdk_iotsitewise.types.asset_model_status
    import aws_sdk_iotsitewise.types.id


class CreateAssetModelCompositeModelResponse(TypedDict, closed=True):
    asset_model_composite_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the composed asset model. You can use this ID when you call other IoT SiteWise APIs.</p>"""
    asset_model_composite_model_path: "aws_sdk_iotsitewise.types.asset_model_composite_model_path.AssetModelCompositeModelPath"
    """<p>The path to the composite model listing the parent composite models.</p>"""
    asset_model_status: "aws_sdk_iotsitewise.types.asset_model_status.AssetModelStatus"


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetModelCompositeModelResponse) -> dict:
    out: dict = {}
    out["assetModelCompositeModelId"] = value["asset_model_composite_model_id"]
    import aws_sdk_iotsitewise.types.asset_model_composite_model_path

    out["assetModelCompositeModelPath"] = (
        aws_sdk_iotsitewise.types.asset_model_composite_model_path.serialize_json(
            value["asset_model_composite_model_path"]
        )
    )
    import aws_sdk_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = (
        aws_sdk_iotsitewise.types.asset_model_status.serialize_json(
            value["asset_model_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateAssetModelCompositeModelResponse:
    out: CreateAssetModelCompositeModelResponse = {}  # type: ignore[typeddict-item]
    if "assetModelCompositeModelId" in data:
        out["asset_model_composite_model_id"] = data["assetModelCompositeModelId"]
    else:
        raise DeserializationError(
            "CreateAssetModelCompositeModelResponse.asset_model_composite_model_id required"
        )
    if "assetModelCompositeModelPath" in data:
        import aws_sdk_iotsitewise.types.asset_model_composite_model_path

        out["asset_model_composite_model_path"] = (
            aws_sdk_iotsitewise.types.asset_model_composite_model_path.deserialize_json(
                data["assetModelCompositeModelPath"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAssetModelCompositeModelResponse.asset_model_composite_model_path required"
        )
    if "assetModelStatus" in data:
        import aws_sdk_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            aws_sdk_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAssetModelCompositeModelResponse.asset_model_status required"
        )
    return out
