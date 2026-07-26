"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.feature_description
    import capo_sagemaker.types.feature_group_arn
    import capo_sagemaker.types.feature_group_name
    import capo_sagemaker.types.feature_name
    import capo_sagemaker.types.feature_parameters
    import capo_sagemaker.types.feature_type
    import capo_sagemaker.types.last_modified_time


class FeatureMetadata(TypedDict, closed=True):
    feature_group_arn: NotRequired[
        "capo_sagemaker.types.feature_group_arn.FeatureGroupArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the feature group.</p>"""
    feature_group_name: NotRequired[
        "capo_sagemaker.types.feature_group_name.FeatureGroupName"
    ]
    """<p>The name of the feature group containing the feature.</p>"""
    feature_name: NotRequired["capo_sagemaker.types.feature_name.FeatureName"]
    """<p>The name of feature.</p>"""
    feature_type: NotRequired["capo_sagemaker.types.feature_type.FeatureType"]
    """<p>The data type of the feature.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp indicating when the feature was created.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp indicating when the feature was last modified.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.feature_description.FeatureDescription"
    ]
    """<p>An optional description that you specify to better describe the feature.</p>"""
    parameters: NotRequired["capo_sagemaker.types.feature_parameters.FeatureParameters"]
    """<p>Optional key-value pairs that you specify to better describe the feature.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureMetadata) -> dict:
    out: dict = {}
    if "feature_group_arn" in value:
        out["FeatureGroupArn"] = value["feature_group_arn"]
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "feature_name" in value:
        out["FeatureName"] = value["feature_name"]
    if "feature_type" in value:
        import capo_sagemaker.types.feature_type

        out["FeatureType"] = capo_sagemaker.types.feature_type.serialize_aws_json_1_1(
            value["feature_type"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "parameters" in value:
        import capo_sagemaker.types.feature_parameters

        out["Parameters"] = (
            capo_sagemaker.types.feature_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureMetadata:
    out: FeatureMetadata = {}  # type: ignore[typeddict-item]
    if "FeatureGroupArn" in data:
        out["feature_group_arn"] = data["FeatureGroupArn"]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "FeatureName" in data:
        out["feature_name"] = data["FeatureName"]
    if "FeatureType" in data:
        import capo_sagemaker.types.feature_type

        out["feature_type"] = (
            capo_sagemaker.types.feature_type.deserialize_aws_json_1_1(
                data["FeatureType"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Parameters" in data:
        import capo_sagemaker.types.feature_parameters

        out["parameters"] = (
            capo_sagemaker.types.feature_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
