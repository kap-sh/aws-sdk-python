"""Generated from Smithy shape ``com.amazonaws.outposts#AssetInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_id
    import aws_sdk_outposts.types.asset_location
    import aws_sdk_outposts.types.asset_type
    import aws_sdk_outposts.types.compute_attributes
    import aws_sdk_outposts.types.rack_id


class AssetInfo(TypedDict, closed=True):
    asset_id: NotRequired["aws_sdk_outposts.types.asset_id.AssetId"]
    """<p> The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>"""
    rack_id: NotRequired["aws_sdk_outposts.types.rack_id.RackId"]
    """<p> The rack ID of the asset. </p>"""
    asset_type: NotRequired["aws_sdk_outposts.types.asset_type.AssetType"]
    """<p> The type of the asset. </p>"""
    compute_attributes: NotRequired[
        "aws_sdk_outposts.types.compute_attributes.ComputeAttributes"
    ]
    """<p> Information about compute hardware assets. </p>"""
    asset_location: NotRequired["aws_sdk_outposts.types.asset_location.AssetLocation"]
    """<p> The position of an asset in a rack. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetInfo) -> dict:
    out: dict = {}
    if "asset_id" in value:
        out["AssetId"] = value["asset_id"]
    if "rack_id" in value:
        out["RackId"] = value["rack_id"]
    if "asset_type" in value:
        import aws_sdk_outposts.types.asset_type

        out["AssetType"] = aws_sdk_outposts.types.asset_type.serialize_json(
            value["asset_type"]
        )
    if "compute_attributes" in value:
        import aws_sdk_outposts.types.compute_attributes

        out["ComputeAttributes"] = (
            aws_sdk_outposts.types.compute_attributes.serialize_json(
                value["compute_attributes"]
            )
        )
    if "asset_location" in value:
        import aws_sdk_outposts.types.asset_location

        out["AssetLocation"] = aws_sdk_outposts.types.asset_location.serialize_json(
            value["asset_location"]
        )
    return out


def deserialize_json(data: dict) -> AssetInfo:
    out: AssetInfo = {}  # type: ignore[typeddict-item]
    if "AssetId" in data:
        out["asset_id"] = data["AssetId"]
    if "RackId" in data:
        out["rack_id"] = data["RackId"]
    if "AssetType" in data:
        import aws_sdk_outposts.types.asset_type

        out["asset_type"] = aws_sdk_outposts.types.asset_type.deserialize_json(
            data["AssetType"]
        )
    if "ComputeAttributes" in data:
        import aws_sdk_outposts.types.compute_attributes

        out["compute_attributes"] = (
            aws_sdk_outposts.types.compute_attributes.deserialize_json(
                data["ComputeAttributes"]
            )
        )
    if "AssetLocation" in data:
        import aws_sdk_outposts.types.asset_location

        out["asset_location"] = aws_sdk_outposts.types.asset_location.deserialize_json(
            data["AssetLocation"]
        )
    return out
