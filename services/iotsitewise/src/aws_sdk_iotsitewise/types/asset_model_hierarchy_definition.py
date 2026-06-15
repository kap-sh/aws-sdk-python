"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelHierarchyDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.custom_id
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name


class AssetModelHierarchyDefinition(TypedDict):
    id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID to assign to the asset model hierarchy, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>"""
    external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    r"""<p>An external ID to assign to the asset model hierarchy. The external ID must be unique among asset model hierarchies within this asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "aws_sdk_iotsitewise.types.name.Name"
    r"""<p>The name of the asset model hierarchy definition (as specified in the <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html\">CreateAssetModel</a> or <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html\">UpdateAssetModel</a> API operation).</p>"""
    child_asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID"
    r"""<p>The ID of an asset model for this hierarchy. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelHierarchyDefinition) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["name"] = value["name"]
    out["childAssetModelId"] = value["child_asset_model_id"]
    return out


def deserialize_json(data: dict) -> AssetModelHierarchyDefinition:
    out: AssetModelHierarchyDefinition = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelHierarchyDefinition.name required")
    if "childAssetModelId" in data:
        out["child_asset_model_id"] = data["childAssetModelId"]
    else:
        raise DeserializationError(
            "AssetModelHierarchyDefinition.child_asset_model_id required"
        )
    return out
