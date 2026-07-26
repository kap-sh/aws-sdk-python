"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_status


class UpdateAssetResponse(TypedDict, closed=True):
    asset_status: "capo_iotsitewise.types.asset_status.AssetStatus"
    """<p>The status of the asset, which contains a state (<code>UPDATING</code> after successfully calling this operation) and any error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_status

    out["assetStatus"] = capo_iotsitewise.types.asset_status.serialize_json(
        value["asset_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAssetResponse:
    out: UpdateAssetResponse = {}  # type: ignore[typeddict-item]
    if "assetStatus" in data:
        import capo_iotsitewise.types.asset_status

        out["asset_status"] = capo_iotsitewise.types.asset_status.deserialize_json(
            data["assetStatus"]
        )
    else:
        raise DeserializationError("UpdateAssetResponse.asset_status required")
    return out
