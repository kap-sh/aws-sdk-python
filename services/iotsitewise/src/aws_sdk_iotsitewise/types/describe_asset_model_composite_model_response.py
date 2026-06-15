"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetModelCompositeModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.action_definitions
    import aws_sdk_iotsitewise.types.asset_model_composite_model_path
    import aws_sdk_iotsitewise.types.asset_model_composite_model_summaries
    import aws_sdk_iotsitewise.types.asset_model_properties
    import aws_sdk_iotsitewise.types.composition_details
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name


class DescribeAssetModelCompositeModelResponse(TypedDict):
    asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    asset_model_composite_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of a composite model on this asset model.</p>"""
    asset_model_composite_model_external_id: NotRequired[
        "aws_sdk_iotsitewise.types.external_id.ExternalId"
    ]
    """<p>The external ID of a composite model on this asset model.</p>"""
    asset_model_composite_model_path: "aws_sdk_iotsitewise.types.asset_model_composite_model_path.AssetModelCompositeModelPath"
    """<p>The path to the composite model listing the parent composite models.</p>"""
    asset_model_composite_model_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The unique, friendly name for the composite model.</p>"""
    asset_model_composite_model_description: (
        "aws_sdk_iotsitewise.types.description.Description"
    )
    """<p>The description for the composite model.</p>"""
    asset_model_composite_model_type: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The composite model type. Valid values are <code>AWS/ALARM</code>, <code>CUSTOM</code>, or <code> AWS/L4E_ANOMALY</code>.</p>"""
    asset_model_composite_model_properties: (
        "aws_sdk_iotsitewise.types.asset_model_properties.AssetModelProperties"
    )
    """<p>The property definitions of the composite model.</p>"""
    composition_details: NotRequired[
        "aws_sdk_iotsitewise.types.composition_details.CompositionDetails"
    ]
    r"""<p>Metadata for the composition relationship established by using <code>composedAssetModelId</code> in <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html\"> <code>CreateAssetModelCompositeModel</code> </a>. For instance, an array detailing the path of the composition relationship for this composite model.</p>"""
    asset_model_composite_model_summaries: "aws_sdk_iotsitewise.types.asset_model_composite_model_summaries.AssetModelCompositeModelSummaries"
    """<p>The list of composite model summaries for the composite model.</p>"""
    action_definitions: NotRequired[
        "aws_sdk_iotsitewise.types.action_definitions.ActionDefinitions"
    ]
    """<p>The available actions for a composite model on this asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetModelCompositeModelResponse) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["assetModelCompositeModelId"] = value["asset_model_composite_model_id"]
    if "asset_model_composite_model_external_id" in value:
        out["assetModelCompositeModelExternalId"] = value[
            "asset_model_composite_model_external_id"
        ]
    import aws_sdk_iotsitewise.types.asset_model_composite_model_path

    out["assetModelCompositeModelPath"] = (
        aws_sdk_iotsitewise.types.asset_model_composite_model_path.serialize_json(
            value["asset_model_composite_model_path"]
        )
    )
    out["assetModelCompositeModelName"] = value["asset_model_composite_model_name"]
    out["assetModelCompositeModelDescription"] = value[
        "asset_model_composite_model_description"
    ]
    out["assetModelCompositeModelType"] = value["asset_model_composite_model_type"]
    import aws_sdk_iotsitewise.types.asset_model_properties

    out["assetModelCompositeModelProperties"] = (
        aws_sdk_iotsitewise.types.asset_model_properties.serialize_json(
            value["asset_model_composite_model_properties"]
        )
    )
    if "composition_details" in value:
        import aws_sdk_iotsitewise.types.composition_details

        out["compositionDetails"] = (
            aws_sdk_iotsitewise.types.composition_details.serialize_json(
                value["composition_details"]
            )
        )
    import aws_sdk_iotsitewise.types.asset_model_composite_model_summaries

    out["assetModelCompositeModelSummaries"] = (
        aws_sdk_iotsitewise.types.asset_model_composite_model_summaries.serialize_json(
            value["asset_model_composite_model_summaries"]
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


def deserialize_json(data: dict) -> DescribeAssetModelCompositeModelResponse:
    out: DescribeAssetModelCompositeModelResponse = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_id required"
        )
    if "assetModelCompositeModelId" in data:
        out["asset_model_composite_model_id"] = data["assetModelCompositeModelId"]
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_id required"
        )
    if "assetModelCompositeModelExternalId" in data:
        out["asset_model_composite_model_external_id"] = data[
            "assetModelCompositeModelExternalId"
        ]
    if "assetModelCompositeModelPath" in data:
        import aws_sdk_iotsitewise.types.asset_model_composite_model_path

        out["asset_model_composite_model_path"] = (
            aws_sdk_iotsitewise.types.asset_model_composite_model_path.deserialize_json(
                data["assetModelCompositeModelPath"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_path required"
        )
    if "assetModelCompositeModelName" in data:
        out["asset_model_composite_model_name"] = data["assetModelCompositeModelName"]
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_name required"
        )
    if "assetModelCompositeModelDescription" in data:
        out["asset_model_composite_model_description"] = data[
            "assetModelCompositeModelDescription"
        ]
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_description required"
        )
    if "assetModelCompositeModelType" in data:
        out["asset_model_composite_model_type"] = data["assetModelCompositeModelType"]
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_type required"
        )
    if "assetModelCompositeModelProperties" in data:
        import aws_sdk_iotsitewise.types.asset_model_properties

        out["asset_model_composite_model_properties"] = (
            aws_sdk_iotsitewise.types.asset_model_properties.deserialize_json(
                data["assetModelCompositeModelProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_properties required"
        )
    if "compositionDetails" in data:
        import aws_sdk_iotsitewise.types.composition_details

        out["composition_details"] = (
            aws_sdk_iotsitewise.types.composition_details.deserialize_json(
                data["compositionDetails"]
            )
        )
    if "assetModelCompositeModelSummaries" in data:
        import aws_sdk_iotsitewise.types.asset_model_composite_model_summaries

        out["asset_model_composite_model_summaries"] = (
            aws_sdk_iotsitewise.types.asset_model_composite_model_summaries.deserialize_json(
                data["assetModelCompositeModelSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelCompositeModelResponse.asset_model_composite_model_summaries required"
        )
    if "actionDefinitions" in data:
        import aws_sdk_iotsitewise.types.action_definitions

        out["action_definitions"] = (
            aws_sdk_iotsitewise.types.action_definitions.deserialize_json(
                data["actionDefinitions"]
            )
        )
    return out
