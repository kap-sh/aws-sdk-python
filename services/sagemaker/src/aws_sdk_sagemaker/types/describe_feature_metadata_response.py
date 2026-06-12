"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeFeatureMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.feature_description
    import aws_sdk_sagemaker.types.feature_group_arn
    import aws_sdk_sagemaker.types.feature_group_name
    import aws_sdk_sagemaker.types.feature_name
    import aws_sdk_sagemaker.types.feature_parameters
    import aws_sdk_sagemaker.types.feature_type
    import aws_sdk_sagemaker.types.last_modified_time


class DescribeFeatureMetadataResponse(TypedDict):
    feature_group_arn: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_arn.FeatureGroupArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the feature group that contains the feature.</p>"""
    feature_group_name: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_name.FeatureGroupName"
    ]
    """<p>The name of the feature group that you've specified.</p>"""
    feature_name: NotRequired["aws_sdk_sagemaker.types.feature_name.FeatureName"]
    """<p>The name of the feature that you've specified.</p>"""
    feature_type: NotRequired["aws_sdk_sagemaker.types.feature_type.FeatureType"]
    """<p>The data type of the feature.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp indicating when the feature was created.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp indicating when the metadata for the feature group was modified. For example, if you add a parameter describing the feature, the timestamp changes to reflect the last time you </p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.feature_description.FeatureDescription"
    ]
    """<p>The description you added to describe the feature.</p>"""
    parameters: NotRequired[
        "aws_sdk_sagemaker.types.feature_parameters.FeatureParameters"
    ]
    """<p>The key-value pairs that you added to describe the feature.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeatureMetadataResponse) -> dict:
    out: dict = {}
    if "feature_group_arn" in value:
        out["FeatureGroupArn"] = value["feature_group_arn"]
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "feature_name" in value:
        out["FeatureName"] = value["feature_name"]
    if "feature_type" in value:
        import aws_sdk_sagemaker.types.feature_type

        out["FeatureType"] = (
            aws_sdk_sagemaker.types.feature_type.serialize_aws_json_1_1(
                value["feature_type"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "parameters" in value:
        import aws_sdk_sagemaker.types.feature_parameters

        out["Parameters"] = (
            aws_sdk_sagemaker.types.feature_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeatureMetadataResponse:
    out: DescribeFeatureMetadataResponse = {}  # type: ignore[typeddict-item]
    if "FeatureGroupArn" in data:
        out["feature_group_arn"] = data["FeatureGroupArn"]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "FeatureName" in data:
        out["feature_name"] = data["FeatureName"]
    if "FeatureType" in data:
        import aws_sdk_sagemaker.types.feature_type

        out["feature_type"] = (
            aws_sdk_sagemaker.types.feature_type.deserialize_aws_json_1_1(
                data["FeatureType"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Parameters" in data:
        import aws_sdk_sagemaker.types.feature_parameters

        out["parameters"] = (
            aws_sdk_sagemaker.types.feature_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
