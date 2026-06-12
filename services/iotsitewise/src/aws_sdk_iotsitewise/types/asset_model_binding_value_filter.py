"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelBindingValueFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class AssetModelBindingValueFilter(TypedDict):
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model to filter data bindings by. Only data bindings referemncing this specific asset model are matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelBindingValueFilter) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    return out


def deserialize_json(data: dict) -> AssetModelBindingValueFilter:
    out: AssetModelBindingValueFilter = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "AssetModelBindingValueFilter.asset_model_id required"
        )
    return out
