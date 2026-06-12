"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateAssetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.custom_id
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.name


class UpdateAssetRequest(TypedDict):
    asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset to update. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    """<p>An external ID to assign to the asset. The asset must not already have an external ID. The external ID must be unique within your Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    asset_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>A friendly name for the asset.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    asset_description: NotRequired["aws_sdk_iotsitewise.types.description.Description"]
    """<p>A description for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetRequest) -> dict:
    out: dict = {}
    if "asset_external_id" in value:
        out["assetExternalId"] = value["asset_external_id"]
    out["assetName"] = value["asset_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "asset_description" in value:
        out["assetDescription"] = value["asset_description"]
    return out


def deserialize_json(data: dict) -> UpdateAssetRequest:
    out: UpdateAssetRequest = {}  # type: ignore[typeddict-item]
    if "assetExternalId" in data:
        out["asset_external_id"] = data["assetExternalId"]
    if "assetName" in data:
        out["asset_name"] = data["assetName"]
    else:
        raise DeserializationError("UpdateAssetRequest.asset_name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "assetDescription" in data:
        out["asset_description"] = data["assetDescription"]
    return out
