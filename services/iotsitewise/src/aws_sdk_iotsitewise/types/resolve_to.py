"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResolveTo``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class ResolveTo(TypedDict):
    asset_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset that the resource resolves to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolveTo) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    return out


def deserialize_json(data: dict) -> ResolveTo:
    out: ResolveTo = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("ResolveTo.asset_id required")
    return out
