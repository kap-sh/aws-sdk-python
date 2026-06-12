"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteAssetModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_status


class DeleteAssetModelResponse(TypedDict):
    asset_model_status: "aws_sdk_iotsitewise.types.asset_model_status.AssetModelStatus"
    """<p>The status of the asset model, which contains a state (<code>DELETING</code> after successfully calling this operation) and any error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetModelResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = (
        aws_sdk_iotsitewise.types.asset_model_status.serialize_json(
            value["asset_model_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteAssetModelResponse:
    out: DeleteAssetModelResponse = {}  # type: ignore[typeddict-item]
    if "assetModelStatus" in data:
        import aws_sdk_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            aws_sdk_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteAssetModelResponse.asset_model_status required"
        )
    return out
