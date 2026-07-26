"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_status


class DeleteAssetResponse(TypedDict, closed=True):
    asset_status: "capo_iotsitewise.types.asset_status.AssetStatus"
    """<p>The status of the asset, which contains a state (<code>DELETING</code> after successfully calling this operation) and any error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_status

    out["assetStatus"] = capo_iotsitewise.types.asset_status.serialize_json(
        value["asset_status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteAssetResponse:
    out: DeleteAssetResponse = {}  # type: ignore[typeddict-item]
    if "assetStatus" in data:
        import capo_iotsitewise.types.asset_status

        out["asset_status"] = capo_iotsitewise.types.asset_status.deserialize_json(
            data["assetStatus"]
        )
    else:
        raise DeserializationError("DeleteAssetResponse.asset_status required")
    return out
