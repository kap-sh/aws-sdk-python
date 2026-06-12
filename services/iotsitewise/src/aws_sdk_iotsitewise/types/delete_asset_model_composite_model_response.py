"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteAssetModelCompositeModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_status


class DeleteAssetModelCompositeModelResponse(TypedDict):
    asset_model_status: "aws_sdk_iotsitewise.types.asset_model_status.AssetModelStatus"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetModelCompositeModelResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = (
        aws_sdk_iotsitewise.types.asset_model_status.serialize_json(
            value["asset_model_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteAssetModelCompositeModelResponse:
    out: DeleteAssetModelCompositeModelResponse = {}  # type: ignore[typeddict-item]
    if "assetModelStatus" in data:
        import aws_sdk_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            aws_sdk_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteAssetModelCompositeModelResponse.asset_model_status required"
        )
    return out
