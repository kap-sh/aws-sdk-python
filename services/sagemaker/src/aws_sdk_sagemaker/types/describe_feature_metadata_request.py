"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeFeatureMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_group_name_or_arn
    import aws_sdk_sagemaker.types.feature_name


class DescribeFeatureMetadataRequest(TypedDict):
    feature_group_name: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the feature group containing the feature.</p>"""
    feature_name: NotRequired["aws_sdk_sagemaker.types.feature_name.FeatureName"]
    """<p>The name of the feature.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeatureMetadataRequest) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "feature_name" in value:
        out["FeatureName"] = value["feature_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeatureMetadataRequest:
    out: DescribeFeatureMetadataRequest = {}  # type: ignore[typeddict-item]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "FeatureName" in data:
        out["feature_name"] = data["FeatureName"]
    return out
