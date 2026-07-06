"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.asset_model_composite_model_summaries
    import aws_sdk_iotsitewise.types.asset_model_composite_models
    import aws_sdk_iotsitewise.types.asset_model_hierarchies
    import aws_sdk_iotsitewise.types.asset_model_properties
    import aws_sdk_iotsitewise.types.asset_model_status
    import aws_sdk_iotsitewise.types.asset_model_type
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.e_tag
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.interface_details
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.timestamp
    import aws_sdk_iotsitewise.types.version


class DescribeAssetModelResponse(TypedDict, closed=True):
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    asset_model_external_id: NotRequired[
        "aws_sdk_iotsitewise.types.external_id.ExternalId"
    ]
    """<p>The external ID of the asset model, if any.</p>"""
    asset_model_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the asset model, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}</code> </p>"""
    asset_model_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the asset model.</p>"""
    asset_model_type: NotRequired[
        "aws_sdk_iotsitewise.types.asset_model_type.AssetModelType"
    ]
    """<p>The type of asset model.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> </ul>"""
    asset_model_description: "aws_sdk_iotsitewise.types.description.Description"
    """<p>The asset model's description.</p>"""
    asset_model_properties: (
        "aws_sdk_iotsitewise.types.asset_model_properties.AssetModelProperties"
    )
    """<p>The list of asset properties for the asset model.</p> <p>This object doesn't include properties that you define in composite models. You can find composite model properties in the <code>assetModelCompositeModels</code> object.</p>"""
    asset_model_hierarchies: (
        "aws_sdk_iotsitewise.types.asset_model_hierarchies.AssetModelHierarchies"
    )
    """<p>A list of asset model hierarchies that each contain a <code>childAssetModelId</code> and a <code>hierarchyId</code> (named <code>id</code>). A hierarchy specifies allowed parent/child asset relationships for an asset model.</p>"""
    asset_model_composite_models: NotRequired[
        "aws_sdk_iotsitewise.types.asset_model_composite_models.AssetModelCompositeModels"
    ]
    """<p>The list of built-in composite models for the asset model, such as those with those of type <code>AWS/ALARMS</code>.</p>"""
    asset_model_composite_model_summaries: NotRequired[
        "aws_sdk_iotsitewise.types.asset_model_composite_model_summaries.AssetModelCompositeModelSummaries"
    ]
    """<p>The list of the immediate child custom composite model summaries for the asset model.</p>"""
    asset_model_creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset model was created, in Unix epoch time.</p>"""
    asset_model_last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the asset model was last updated, in Unix epoch time.</p>"""
    asset_model_status: "aws_sdk_iotsitewise.types.asset_model_status.AssetModelStatus"
    """<p>The current status of the asset model, which contains a state and any error message.</p>"""
    asset_model_version: NotRequired["aws_sdk_iotsitewise.types.version.Version"]
    r"""<p>The version of the asset model. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html\"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    interface_details: NotRequired[
        "aws_sdk_iotsitewise.types.interface_details.InterfaceDetails"
    ]
    """<p>A list of interface details that describe the interfaces implemented by this asset model, including interface asset model IDs and property mappings.</p>"""
    e_tag: NotRequired["aws_sdk_iotsitewise.types.e_tag.ETag"]
    r"""<p>The entity tag (ETag) is a hash of the retrieved version of the asset model. It's used to make concurrent updates safely to the resource. See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html\">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>. </p> <p>See <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html\"> Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetModelResponse) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    if "asset_model_external_id" in value:
        out["assetModelExternalId"] = value["asset_model_external_id"]
    out["assetModelArn"] = value["asset_model_arn"]
    out["assetModelName"] = value["asset_model_name"]
    if "asset_model_type" in value:
        import aws_sdk_iotsitewise.types.asset_model_type

        out["assetModelType"] = (
            aws_sdk_iotsitewise.types.asset_model_type.serialize_json(
                value["asset_model_type"]
            )
        )
    out["assetModelDescription"] = value["asset_model_description"]
    import aws_sdk_iotsitewise.types.asset_model_properties

    out["assetModelProperties"] = (
        aws_sdk_iotsitewise.types.asset_model_properties.serialize_json(
            value["asset_model_properties"]
        )
    )
    import aws_sdk_iotsitewise.types.asset_model_hierarchies

    out["assetModelHierarchies"] = (
        aws_sdk_iotsitewise.types.asset_model_hierarchies.serialize_json(
            value["asset_model_hierarchies"]
        )
    )
    if "asset_model_composite_models" in value:
        import aws_sdk_iotsitewise.types.asset_model_composite_models

        out["assetModelCompositeModels"] = (
            aws_sdk_iotsitewise.types.asset_model_composite_models.serialize_json(
                value["asset_model_composite_models"]
            )
        )
    if "asset_model_composite_model_summaries" in value:
        import aws_sdk_iotsitewise.types.asset_model_composite_model_summaries

        out["assetModelCompositeModelSummaries"] = (
            aws_sdk_iotsitewise.types.asset_model_composite_model_summaries.serialize_json(
                value["asset_model_composite_model_summaries"]
            )
        )
    import aws_sdk_iotsitewise.types.timestamp

    out["assetModelCreationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["asset_model_creation_date"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["assetModelLastUpdateDate"] = (
        aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["asset_model_last_update_date"]
        )
    )
    import aws_sdk_iotsitewise.types.asset_model_status

    out["assetModelStatus"] = (
        aws_sdk_iotsitewise.types.asset_model_status.serialize_json(
            value["asset_model_status"]
        )
    )
    if "asset_model_version" in value:
        out["assetModelVersion"] = value["asset_model_version"]
    if "interface_details" in value:
        import aws_sdk_iotsitewise.types.interface_details

        out["interfaceDetails"] = (
            aws_sdk_iotsitewise.types.interface_details.serialize_json(
                value["interface_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetModelResponse:
    out: DescribeAssetModelResponse = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError("DescribeAssetModelResponse.asset_model_id required")
    if "assetModelExternalId" in data:
        out["asset_model_external_id"] = data["assetModelExternalId"]
    if "assetModelArn" in data:
        out["asset_model_arn"] = data["assetModelArn"]
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_arn required"
        )
    if "assetModelName" in data:
        out["asset_model_name"] = data["assetModelName"]
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_name required"
        )
    if "assetModelType" in data:
        import aws_sdk_iotsitewise.types.asset_model_type

        out["asset_model_type"] = (
            aws_sdk_iotsitewise.types.asset_model_type.deserialize_json(
                data["assetModelType"]
            )
        )
    if "assetModelDescription" in data:
        out["asset_model_description"] = data["assetModelDescription"]
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_description required"
        )
    if "assetModelProperties" in data:
        import aws_sdk_iotsitewise.types.asset_model_properties

        out["asset_model_properties"] = (
            aws_sdk_iotsitewise.types.asset_model_properties.deserialize_json(
                data["assetModelProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_properties required"
        )
    if "assetModelHierarchies" in data:
        import aws_sdk_iotsitewise.types.asset_model_hierarchies

        out["asset_model_hierarchies"] = (
            aws_sdk_iotsitewise.types.asset_model_hierarchies.deserialize_json(
                data["assetModelHierarchies"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_hierarchies required"
        )
    if "assetModelCompositeModels" in data:
        import aws_sdk_iotsitewise.types.asset_model_composite_models

        out["asset_model_composite_models"] = (
            aws_sdk_iotsitewise.types.asset_model_composite_models.deserialize_json(
                data["assetModelCompositeModels"]
            )
        )
    if "assetModelCompositeModelSummaries" in data:
        import aws_sdk_iotsitewise.types.asset_model_composite_model_summaries

        out["asset_model_composite_model_summaries"] = (
            aws_sdk_iotsitewise.types.asset_model_composite_model_summaries.deserialize_json(
                data["assetModelCompositeModelSummaries"]
            )
        )
    if "assetModelCreationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["asset_model_creation_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["assetModelCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_creation_date required"
        )
    if "assetModelLastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["asset_model_last_update_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["assetModelLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelResponse.asset_model_last_update_date required"
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
            "DescribeAssetModelResponse.asset_model_status required"
        )
    if "assetModelVersion" in data:
        out["asset_model_version"] = data["assetModelVersion"]
    if "interfaceDetails" in data:
        import aws_sdk_iotsitewise.types.interface_details

        out["interface_details"] = (
            aws_sdk_iotsitewise.types.interface_details.deserialize_json(
                data["interfaceDetails"]
            )
        )
    return out
