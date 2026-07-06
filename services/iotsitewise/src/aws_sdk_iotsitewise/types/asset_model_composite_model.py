"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelCompositeModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_properties
    import aws_sdk_iotsitewise.types.custom_id
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.name


class AssetModelCompositeModel(TypedDict, closed=True):
    name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the composite model.</p>"""
    description: NotRequired["aws_sdk_iotsitewise.types.description.Description"]
    """<p>The description of the composite model.</p>"""
    type: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The type of the composite model. For alarm composite models, this type is <code>AWS/ALARM</code>.</p>"""
    properties: NotRequired[
        "aws_sdk_iotsitewise.types.asset_model_properties.AssetModelProperties"
    ]
    """<p>The asset property definitions for this composite model.</p>"""
    id: NotRequired["aws_sdk_iotsitewise.types.custom_id.CustomID"]
    """<p> The ID of the asset model composite model. </p>"""
    external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    r"""<p>The external ID of the asset model composite model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelCompositeModel) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["type"] = value["type"]
    if "properties" in value:
        import aws_sdk_iotsitewise.types.asset_model_properties

        out["properties"] = (
            aws_sdk_iotsitewise.types.asset_model_properties.serialize_json(
                value["properties"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> AssetModelCompositeModel:
    out: AssetModelCompositeModel = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelCompositeModel.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AssetModelCompositeModel.type required")
    if "properties" in data:
        import aws_sdk_iotsitewise.types.asset_model_properties

        out["properties"] = (
            aws_sdk_iotsitewise.types.asset_model_properties.deserialize_json(
                data["properties"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    return out
