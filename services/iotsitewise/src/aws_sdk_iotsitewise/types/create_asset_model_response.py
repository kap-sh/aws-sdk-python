"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateAssetModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.asset_model_status
    import aws_sdk_iotsitewise.types.id


class CreateAssetModelResponse(TypedDict):
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format. You can use this ID when you call other IoT SiteWise API operations.</p>"""
    asset_model_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the asset model, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}</code> </p>"""
    asset_model_status: "aws_sdk_iotsitewise.types.asset_model_status.AssetModelStatus"
    """<p>The status of the asset model, which contains a state (<code>CREATING</code> after successfully calling this operation) and any error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetModelResponse) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["assetModelArn"] = value["asset_model_arn"]
    import aws_sdk_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = (
        aws_sdk_iotsitewise.types.asset_model_status.serialize_json(
            value["asset_model_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateAssetModelResponse:
    out: CreateAssetModelResponse = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError("CreateAssetModelResponse.asset_model_id required")
    if "assetModelArn" in data:
        out["asset_model_arn"] = data["assetModelArn"]
    else:
        raise DeserializationError("CreateAssetModelResponse.asset_model_arn required")
    if "assetModelStatus" in data:
        import aws_sdk_iotsitewise.types.asset_model_status

        out["asset_model_status"] = (
            aws_sdk_iotsitewise.types.asset_model_status.deserialize_json(
                data["assetModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAssetModelResponse.asset_model_status required"
        )
    return out
