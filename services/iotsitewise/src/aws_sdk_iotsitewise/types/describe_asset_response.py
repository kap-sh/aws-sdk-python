"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.asset_composite_model_summaries
    import aws_sdk_iotsitewise.types.asset_composite_models
    import aws_sdk_iotsitewise.types.asset_hierarchies
    import aws_sdk_iotsitewise.types.asset_properties
    import aws_sdk_iotsitewise.types.asset_status
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.timestamp


class DescribeAssetResponse(TypedDict, closed=True):
    asset_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset, in UUID format.</p>"""
    asset_external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the asset, if any.</p>"""
    asset_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the asset, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}</code> </p>"""
    asset_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the asset.</p>"""
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model that was used to create the asset.</p>"""
    asset_properties: "aws_sdk_iotsitewise.types.asset_properties.AssetProperties"
    """<p>The list of asset properties for the asset.</p> <p>This object doesn't include properties that you define in composite models. You can find composite model properties in the <code>assetCompositeModels</code> object.</p>"""
    asset_hierarchies: "aws_sdk_iotsitewise.types.asset_hierarchies.AssetHierarchies"
    """<p>A list of asset hierarchies that each contain a <code>hierarchyId</code>. A hierarchy specifies allowed parent/child asset relationships.</p>"""
    asset_composite_models: NotRequired[
        "aws_sdk_iotsitewise.types.asset_composite_models.AssetCompositeModels"
    ]
    """<p>The composite models for the asset.</p>"""
    asset_creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset was created, in Unix epoch time.</p>"""
    asset_last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset was last updated, in Unix epoch time.</p>"""
    asset_status: "aws_sdk_iotsitewise.types.asset_status.AssetStatus"
    """<p>The current status of the asset, which contains a state and any error message.</p>"""
    asset_description: NotRequired["aws_sdk_iotsitewise.types.description.Description"]
    """<p>A description for the asset.</p>"""
    asset_composite_model_summaries: NotRequired[
        "aws_sdk_iotsitewise.types.asset_composite_model_summaries.AssetCompositeModelSummaries"
    ]
    """<p>The list of the immediate child custom composite model summaries for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetResponse) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    if "asset_external_id" in value:
        out["assetExternalId"] = value["asset_external_id"]
    out["assetArn"] = value["asset_arn"]
    out["assetName"] = value["asset_name"]
    out["assetModelId"] = value["asset_model_id"]
    import aws_sdk_iotsitewise.types.asset_properties

    out["assetProperties"] = aws_sdk_iotsitewise.types.asset_properties.serialize_json(
        value["asset_properties"]
    )
    import aws_sdk_iotsitewise.types.asset_hierarchies

    out["assetHierarchies"] = (
        aws_sdk_iotsitewise.types.asset_hierarchies.serialize_json(
            value["asset_hierarchies"]
        )
    )
    if "asset_composite_models" in value:
        import aws_sdk_iotsitewise.types.asset_composite_models

        out["assetCompositeModels"] = (
            aws_sdk_iotsitewise.types.asset_composite_models.serialize_json(
                value["asset_composite_models"]
            )
        )
    import aws_sdk_iotsitewise.types.timestamp

    out["assetCreationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["asset_creation_date"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["assetLastUpdateDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["asset_last_update_date"]
    )
    import aws_sdk_iotsitewise.types.asset_status

    out["assetStatus"] = aws_sdk_iotsitewise.types.asset_status.serialize_json(
        value["asset_status"]
    )
    if "asset_description" in value:
        out["assetDescription"] = value["asset_description"]
    if "asset_composite_model_summaries" in value:
        import aws_sdk_iotsitewise.types.asset_composite_model_summaries

        out["assetCompositeModelSummaries"] = (
            aws_sdk_iotsitewise.types.asset_composite_model_summaries.serialize_json(
                value["asset_composite_model_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetResponse:
    out: DescribeAssetResponse = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("DescribeAssetResponse.asset_id required")
    if "assetExternalId" in data:
        out["asset_external_id"] = data["assetExternalId"]
    if "assetArn" in data:
        out["asset_arn"] = data["assetArn"]
    else:
        raise DeserializationError("DescribeAssetResponse.asset_arn required")
    if "assetName" in data:
        out["asset_name"] = data["assetName"]
    else:
        raise DeserializationError("DescribeAssetResponse.asset_name required")
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError("DescribeAssetResponse.asset_model_id required")
    if "assetProperties" in data:
        import aws_sdk_iotsitewise.types.asset_properties

        out["asset_properties"] = (
            aws_sdk_iotsitewise.types.asset_properties.deserialize_json(
                data["assetProperties"]
            )
        )
    else:
        raise DeserializationError("DescribeAssetResponse.asset_properties required")
    if "assetHierarchies" in data:
        import aws_sdk_iotsitewise.types.asset_hierarchies

        out["asset_hierarchies"] = (
            aws_sdk_iotsitewise.types.asset_hierarchies.deserialize_json(
                data["assetHierarchies"]
            )
        )
    else:
        raise DeserializationError("DescribeAssetResponse.asset_hierarchies required")
    if "assetCompositeModels" in data:
        import aws_sdk_iotsitewise.types.asset_composite_models

        out["asset_composite_models"] = (
            aws_sdk_iotsitewise.types.asset_composite_models.deserialize_json(
                data["assetCompositeModels"]
            )
        )
    if "assetCreationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["asset_creation_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["assetCreationDate"]
            )
        )
    else:
        raise DeserializationError("DescribeAssetResponse.asset_creation_date required")
    if "assetLastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["asset_last_update_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["assetLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetResponse.asset_last_update_date required"
        )
    if "assetStatus" in data:
        import aws_sdk_iotsitewise.types.asset_status

        out["asset_status"] = aws_sdk_iotsitewise.types.asset_status.deserialize_json(
            data["assetStatus"]
        )
    else:
        raise DeserializationError("DescribeAssetResponse.asset_status required")
    if "assetDescription" in data:
        out["asset_description"] = data["assetDescription"]
    if "assetCompositeModelSummaries" in data:
        import aws_sdk_iotsitewise.types.asset_composite_model_summaries

        out["asset_composite_model_summaries"] = (
            aws_sdk_iotsitewise.types.asset_composite_model_summaries.deserialize_json(
                data["assetCompositeModelSummaries"]
            )
        )
    return out
