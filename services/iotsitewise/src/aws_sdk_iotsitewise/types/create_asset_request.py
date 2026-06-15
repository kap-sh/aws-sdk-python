"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateAssetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.custom_id
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.tag_map


class CreateAssetRequest(TypedDict):
    asset_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>A friendly name for the asset.</p>"""
    asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID"
    r"""<p>The ID of the asset model from which to create the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID to assign to the asset, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>"""
    asset_external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    r"""<p>An external ID to assign to the asset. The external ID must be unique within your Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    tags: NotRequired["aws_sdk_iotsitewise.types.tag_map.TagMap"]
    r"""<p>A list of key-value pairs that contain metadata for the asset. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_description: NotRequired["aws_sdk_iotsitewise.types.description.Description"]
    """<p>A description for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetRequest) -> dict:
    out: dict = {}
    out["assetName"] = value["asset_name"]
    out["assetModelId"] = value["asset_model_id"]
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "asset_external_id" in value:
        out["assetExternalId"] = value["asset_external_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_iotsitewise.types.tag_map

        out["tags"] = aws_sdk_iotsitewise.types.tag_map.serialize_json(value["tags"])
    if "asset_description" in value:
        out["assetDescription"] = value["asset_description"]
    return out


def deserialize_json(data: dict) -> CreateAssetRequest:
    out: CreateAssetRequest = {}  # type: ignore[typeddict-item]
    if "assetName" in data:
        out["asset_name"] = data["assetName"]
    else:
        raise DeserializationError("CreateAssetRequest.asset_name required")
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError("CreateAssetRequest.asset_model_id required")
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    if "assetExternalId" in data:
        out["asset_external_id"] = data["assetExternalId"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_iotsitewise.types.tag_map

        out["tags"] = aws_sdk_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    if "assetDescription" in data:
        out["asset_description"] = data["assetDescription"]
    return out
