"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteAssetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_status


class DeleteAssetResponse(TypedDict):
    asset_status: "aws_sdk_iotsitewise.types.asset_status.AssetStatus"
    """<p>The status of the asset, which contains a state (<code>DELETING</code> after successfully calling this operation) and any error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.asset_status

    out["assetStatus"] = aws_sdk_iotsitewise.types.asset_status.serialize_json(
        value["asset_status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteAssetResponse:
    out: DeleteAssetResponse = {}  # type: ignore[typeddict-item]
    if "assetStatus" in data:
        import aws_sdk_iotsitewise.types.asset_status

        out["asset_status"] = aws_sdk_iotsitewise.types.asset_status.deserialize_json(
            data["assetStatus"]
        )
    else:
        raise DeserializationError("DeleteAssetResponse.asset_status required")
    return out
