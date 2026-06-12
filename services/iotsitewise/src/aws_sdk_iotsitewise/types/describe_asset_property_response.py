"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetPropertyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.composite_model_property
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.property


class DescribeAssetPropertyResponse(TypedDict):
    asset_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset, in UUID format.</p>"""
    asset_external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the asset. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the asset.</p>"""
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    asset_property: NotRequired["aws_sdk_iotsitewise.types.property.Property"]
    """<p>The asset property's definition, alias, and notification state.</p> <p>This response includes this object for normal asset properties. If you describe an asset property in a composite model, this response includes the asset property information in <code>compositeModel</code>.</p>"""
    composite_model: NotRequired[
        "aws_sdk_iotsitewise.types.composite_model_property.CompositeModelProperty"
    ]
    """<p>The composite model that declares this asset property, if this asset property exists in a composite model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetPropertyResponse) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    if "asset_external_id" in value:
        out["assetExternalId"] = value["asset_external_id"]
    out["assetName"] = value["asset_name"]
    out["assetModelId"] = value["asset_model_id"]
    if "asset_property" in value:
        import aws_sdk_iotsitewise.types.property

        out["assetProperty"] = aws_sdk_iotsitewise.types.property.serialize_json(
            value["asset_property"]
        )
    if "composite_model" in value:
        import aws_sdk_iotsitewise.types.composite_model_property

        out["compositeModel"] = (
            aws_sdk_iotsitewise.types.composite_model_property.serialize_json(
                value["composite_model"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetPropertyResponse:
    out: DescribeAssetPropertyResponse = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("DescribeAssetPropertyResponse.asset_id required")
    if "assetExternalId" in data:
        out["asset_external_id"] = data["assetExternalId"]
    if "assetName" in data:
        out["asset_name"] = data["assetName"]
    else:
        raise DeserializationError("DescribeAssetPropertyResponse.asset_name required")
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "DescribeAssetPropertyResponse.asset_model_id required"
        )
    if "assetProperty" in data:
        import aws_sdk_iotsitewise.types.property

        out["asset_property"] = aws_sdk_iotsitewise.types.property.deserialize_json(
            data["assetProperty"]
        )
    if "compositeModel" in data:
        import aws_sdk_iotsitewise.types.composite_model_property

        out["composite_model"] = (
            aws_sdk_iotsitewise.types.composite_model_property.deserialize_json(
                data["compositeModel"]
            )
        )
    return out
