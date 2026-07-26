"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateAssetModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_status


class UpdateAssetModelResponse(TypedDict, closed=True):
    asset_model_status: "capo_iotsitewise.types.asset_model_status.AssetModelStatus"
    """<p>The status of the asset model, which contains a state (<code>UPDATING</code> after successfully calling this operation) and any error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetModelResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = capo_iotsitewise.types.asset_model_status.serialize_json(
        value["asset_model_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAssetModelResponse:
    out: UpdateAssetModelResponse = {}  # type: ignore[typeddict-item]
    if "assetModelStatus" in data:
        import capo_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            capo_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssetModelResponse.asset_model_status required"
        )
    return out
