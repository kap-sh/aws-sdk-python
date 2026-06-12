"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TargetResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class TargetResource(TypedDict):
    asset_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the asset, in UUID format.</p>"""
    computation_model_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the computation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetResource) -> dict:
    out: dict = {}
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "computation_model_id" in value:
        out["computationModelId"] = value["computation_model_id"]
    return out


def deserialize_json(data: dict) -> TargetResource:
    out: TargetResource = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    if "computationModelId" in data:
        out["computation_model_id"] = data["computationModelId"]
    return out
