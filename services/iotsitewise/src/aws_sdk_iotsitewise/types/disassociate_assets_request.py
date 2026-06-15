"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DisassociateAssetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.custom_id


class DisassociateAssetsRequest(TypedDict):
    asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID"
    r"""<p>The ID of the parent asset from which to disassociate the child asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    hierarchy_id: "aws_sdk_iotsitewise.types.custom_id.CustomID"
    r"""<p>The ID of a hierarchy in the parent asset's model. (This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.) Hierarchies allow different groupings of assets to be formed that all come from the same asset model. You can use the hierarchy ID to identify the correct asset to disassociate. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    child_asset_id: "aws_sdk_iotsitewise.types.custom_id.CustomID"
    r"""<p>The ID of the child asset to disassociate. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAssetsRequest) -> dict:
    out: dict = {}
    out["hierarchyId"] = value["hierarchy_id"]
    out["childAssetId"] = value["child_asset_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DisassociateAssetsRequest:
    out: DisassociateAssetsRequest = {}  # type: ignore[typeddict-item]
    if "hierarchyId" in data:
        out["hierarchy_id"] = data["hierarchyId"]
    else:
        raise DeserializationError("DisassociateAssetsRequest.hierarchy_id required")
    if "childAssetId" in data:
        out["child_asset_id"] = data["childAssetId"]
    else:
        raise DeserializationError("DisassociateAssetsRequest.child_asset_id required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
