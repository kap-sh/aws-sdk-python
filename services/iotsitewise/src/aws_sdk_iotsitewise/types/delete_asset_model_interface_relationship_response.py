"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteAssetModelInterfaceRelationshipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.asset_model_status
    import aws_sdk_iotsitewise.types.id


class DeleteAssetModelInterfaceRelationshipResponse(TypedDict, closed=True):
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model.</p>"""
    interface_asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the interface asset model.</p>"""
    asset_model_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    """<p>The ARN of the asset model, which has the following format. <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}</code> </p>"""
    asset_model_status: "aws_sdk_iotsitewise.types.asset_model_status.AssetModelStatus"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetModelInterfaceRelationshipResponse) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["interfaceAssetModelId"] = value["interface_asset_model_id"]
    out["assetModelArn"] = value["asset_model_arn"]
    import aws_sdk_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = (
        aws_sdk_iotsitewise.types.asset_model_status.serialize_json(
            value["asset_model_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteAssetModelInterfaceRelationshipResponse:
    out: DeleteAssetModelInterfaceRelationshipResponse = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "DeleteAssetModelInterfaceRelationshipResponse.asset_model_id required"
        )
    if "interfaceAssetModelId" in data:
        out["interface_asset_model_id"] = data["interfaceAssetModelId"]
    else:
        raise DeserializationError(
            "DeleteAssetModelInterfaceRelationshipResponse.interface_asset_model_id required"
        )
    if "assetModelArn" in data:
        out["asset_model_arn"] = data["assetModelArn"]
    else:
        raise DeserializationError(
            "DeleteAssetModelInterfaceRelationshipResponse.asset_model_arn required"
        )
    if "assetModelStatus" in data:
        import aws_sdk_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            aws_sdk_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteAssetModelInterfaceRelationshipResponse.asset_model_status required"
        )
    return out
