"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetBindingValueFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class AssetBindingValueFilter(TypedDict, closed=True):
    asset_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset to filter data bindings by. Only data bindings referencing this specific asset are matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBindingValueFilter) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    return out


def deserialize_json(data: dict) -> AssetBindingValueFilter:
    out: AssetBindingValueFilter = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("AssetBindingValueFilter.asset_id required")
    return out
