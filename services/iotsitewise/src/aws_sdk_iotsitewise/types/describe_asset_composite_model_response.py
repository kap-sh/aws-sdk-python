"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetCompositeModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.action_definitions
    import aws_sdk_iotsitewise.types.asset_composite_model_path
    import aws_sdk_iotsitewise.types.asset_composite_model_summaries
    import aws_sdk_iotsitewise.types.asset_properties
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name


class DescribeAssetCompositeModelResponse(TypedDict, closed=True):
    asset_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset, in UUID format. This ID uniquely identifies the asset within IoT SiteWise and can be used with other IoT SiteWise APIs.</p>"""
    asset_composite_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of a composite model on this asset.</p>"""
    asset_composite_model_external_id: NotRequired[
        "aws_sdk_iotsitewise.types.external_id.ExternalId"
    ]
    """<p>An external ID to assign to the asset model.</p> <p>If the composite model is a component-based composite model, or one nested inside a component model, you can only set the external ID using <code>UpdateAssetModelCompositeModel</code> and specifying the derived ID of the model or property from the created model it's a part of.</p>"""
    asset_composite_model_path: (
        "aws_sdk_iotsitewise.types.asset_composite_model_path.AssetCompositeModelPath"
    )
    """<p>The path to the composite model listing the parent composite models.</p>"""
    asset_composite_model_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The unique, friendly name for the composite model.</p>"""
    asset_composite_model_description: (
        "aws_sdk_iotsitewise.types.description.Description"
    )
    """<p>A description for the composite model.</p>"""
    asset_composite_model_type: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The composite model type. Valid values are <code>AWS/ALARM</code>, <code>CUSTOM</code>, or <code> AWS/L4E_ANOMALY</code>.</p>"""
    asset_composite_model_properties: (
        "aws_sdk_iotsitewise.types.asset_properties.AssetProperties"
    )
    """<p>The property definitions of the composite model that was used to create the asset.</p>"""
    asset_composite_model_summaries: "aws_sdk_iotsitewise.types.asset_composite_model_summaries.AssetCompositeModelSummaries"
    """<p>The list of composite model summaries.</p>"""
    action_definitions: NotRequired[
        "aws_sdk_iotsitewise.types.action_definitions.ActionDefinitions"
    ]
    """<p>The available actions for a composite model on this asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetCompositeModelResponse) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    out["assetCompositeModelId"] = value["asset_composite_model_id"]
    if "asset_composite_model_external_id" in value:
        out["assetCompositeModelExternalId"] = value[
            "asset_composite_model_external_id"
        ]
    import aws_sdk_iotsitewise.types.asset_composite_model_path

    out["assetCompositeModelPath"] = (
        aws_sdk_iotsitewise.types.asset_composite_model_path.serialize_json(
            value["asset_composite_model_path"]
        )
    )
    out["assetCompositeModelName"] = value["asset_composite_model_name"]
    out["assetCompositeModelDescription"] = value["asset_composite_model_description"]
    out["assetCompositeModelType"] = value["asset_composite_model_type"]
    import aws_sdk_iotsitewise.types.asset_properties

    out["assetCompositeModelProperties"] = (
        aws_sdk_iotsitewise.types.asset_properties.serialize_json(
            value["asset_composite_model_properties"]
        )
    )
    import aws_sdk_iotsitewise.types.asset_composite_model_summaries

    out["assetCompositeModelSummaries"] = (
        aws_sdk_iotsitewise.types.asset_composite_model_summaries.serialize_json(
            value["asset_composite_model_summaries"]
        )
    )
    if "action_definitions" in value:
        import aws_sdk_iotsitewise.types.action_definitions

        out["actionDefinitions"] = (
            aws_sdk_iotsitewise.types.action_definitions.serialize_json(
                value["action_definitions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetCompositeModelResponse:
    out: DescribeAssetCompositeModelResponse = {}  # type: ignore[typeddict-item]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError(
            "DescribeAssetCompositeModelResponse.asset_id required"
        )
    if "assetCompositeModelId" in data:
        out["asset_composite_model_id"] = data["assetCompositeModelId"]
    else:
        raise DeserializationError(
            "DescribeAssetCompositeModelResponse.asset_composite_model_id required"
        )
    if "assetCompositeModelExternalId" in data:
        out["asset_composite_model_external_id"] = data["assetCompositeModelExternalId"]
    if "assetCompositeModelPath" in data:
        import aws_sdk_iotsitewise.types.asset_composite_model_path

        out["asset_composite_model_path"] = (
            aws_sdk_iotsitewise.types.asset_composite_model_path.deserialize_json(
                data["assetCompositeModelPath"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetCompositeModelResponse.asset_composite_model_path required"
        )
    if "assetCompositeModelName" in data:
        out["asset_composite_model_name"] = data["assetCompositeModelName"]
    else:
        raise DeserializationError(
            "DescribeAssetCompositeModelResponse.asset_composite_model_name required"
        )
    if "assetCompositeModelDescription" in data:
        out["asset_composite_model_description"] = data[
            "assetCompositeModelDescription"
        ]
    else:
        raise DeserializationError(
            "DescribeAssetCompositeModelResponse.asset_composite_model_description required"
        )
    if "assetCompositeModelType" in data:
        out["asset_composite_model_type"] = data["assetCompositeModelType"]
    else:
        raise DeserializationError(
            "DescribeAssetCompositeModelResponse.asset_composite_model_type required"
        )
    if "assetCompositeModelProperties" in data:
        import aws_sdk_iotsitewise.types.asset_properties

        out["asset_composite_model_properties"] = (
            aws_sdk_iotsitewise.types.asset_properties.deserialize_json(
                data["assetCompositeModelProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetCompositeModelResponse.asset_composite_model_properties required"
        )
    if "assetCompositeModelSummaries" in data:
        import aws_sdk_iotsitewise.types.asset_composite_model_summaries

        out["asset_composite_model_summaries"] = (
            aws_sdk_iotsitewise.types.asset_composite_model_summaries.deserialize_json(
                data["assetCompositeModelSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetCompositeModelResponse.asset_composite_model_summaries required"
        )
    if "actionDefinitions" in data:
        import aws_sdk_iotsitewise.types.action_definitions

        out["action_definitions"] = (
            aws_sdk_iotsitewise.types.action_definitions.deserialize_json(
                data["actionDefinitions"]
            )
        )
    return out
