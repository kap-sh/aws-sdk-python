"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateFeatureMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_description
    import aws_sdk_sagemaker.types.feature_group_name_or_arn
    import aws_sdk_sagemaker.types.feature_name
    import aws_sdk_sagemaker.types.feature_parameter_additions
    import aws_sdk_sagemaker.types.feature_parameter_removals


class UpdateFeatureMetadataRequest(TypedDict):
    feature_group_name: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the feature group containing the feature that you're updating.</p>"""
    feature_name: NotRequired["aws_sdk_sagemaker.types.feature_name.FeatureName"]
    """<p>The name of the feature that you're updating.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.feature_description.FeatureDescription"
    ]
    """<p>A description that you can write to better describe the feature.</p>"""
    parameter_additions: NotRequired[
        "aws_sdk_sagemaker.types.feature_parameter_additions.FeatureParameterAdditions"
    ]
    """<p>A list of key-value pairs that you can add to better describe the feature.</p>"""
    parameter_removals: NotRequired[
        "aws_sdk_sagemaker.types.feature_parameter_removals.FeatureParameterRemovals"
    ]
    """<p>A list of parameter keys that you can specify to remove parameters that describe your feature.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFeatureMetadataRequest) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "feature_name" in value:
        out["FeatureName"] = value["feature_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "parameter_additions" in value:
        import aws_sdk_sagemaker.types.feature_parameter_additions

        out["ParameterAdditions"] = (
            aws_sdk_sagemaker.types.feature_parameter_additions.serialize_aws_json_1_1(
                value["parameter_additions"]
            )
        )
    if "parameter_removals" in value:
        import aws_sdk_sagemaker.types.feature_parameter_removals

        out["ParameterRemovals"] = (
            aws_sdk_sagemaker.types.feature_parameter_removals.serialize_aws_json_1_1(
                value["parameter_removals"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFeatureMetadataRequest:
    out: UpdateFeatureMetadataRequest = {}  # type: ignore[typeddict-item]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "FeatureName" in data:
        out["feature_name"] = data["FeatureName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ParameterAdditions" in data:
        import aws_sdk_sagemaker.types.feature_parameter_additions

        out["parameter_additions"] = (
            aws_sdk_sagemaker.types.feature_parameter_additions.deserialize_aws_json_1_1(
                data["ParameterAdditions"]
            )
        )
    if "ParameterRemovals" in data:
        import aws_sdk_sagemaker.types.feature_parameter_removals

        out["parameter_removals"] = (
            aws_sdk_sagemaker.types.feature_parameter_removals.deserialize_aws_json_1_1(
                data["ParameterRemovals"]
            )
        )
    return out
