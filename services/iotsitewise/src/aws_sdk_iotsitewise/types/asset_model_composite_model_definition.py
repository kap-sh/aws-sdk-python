"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelCompositeModelDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_property_definitions
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name


class AssetModelCompositeModelDefinition(TypedDict):
    id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID to assign to the composite model, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>"""
    external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    """<p>An external ID to assign to the composite model. The external ID must be unique among composite models within this asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the composite model.</p>"""
    description: NotRequired["aws_sdk_iotsitewise.types.description.Description"]
    """<p>The description of the composite model.</p>"""
    type: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The type of the composite model. For alarm composite models, this type is <code>AWS/ALARM</code>.</p>"""
    properties: NotRequired[
        "aws_sdk_iotsitewise.types.asset_model_property_definitions.AssetModelPropertyDefinitions"
    ]
    """<p>The asset property definitions for this composite model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelCompositeModelDefinition) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["type"] = value["type"]
    if "properties" in value:
        import aws_sdk_iotsitewise.types.asset_model_property_definitions

        out["properties"] = (
            aws_sdk_iotsitewise.types.asset_model_property_definitions.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetModelCompositeModelDefinition:
    out: AssetModelCompositeModelDefinition = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelCompositeModelDefinition.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AssetModelCompositeModelDefinition.type required")
    if "properties" in data:
        import aws_sdk_iotsitewise.types.asset_model_property_definitions

        out["properties"] = (
            aws_sdk_iotsitewise.types.asset_model_property_definitions.deserialize_json(
                data["properties"]
            )
        )
    return out
