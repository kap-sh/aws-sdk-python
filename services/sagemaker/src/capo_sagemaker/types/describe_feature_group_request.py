"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeFeatureGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.feature_group_name_or_arn
    import capo_sagemaker.types.next_token


class DescribeFeatureGroupRequest(TypedDict, closed=True):
    feature_group_name: NotRequired[
        "capo_sagemaker.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the <code>FeatureGroup</code> you want described. </p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token to resume pagination of the list of <code>Features</code> (<code>FeatureDefinitions</code>). 2,500 <code>Features</code> are returned by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeatureGroupRequest) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeatureGroupRequest:
    out: DescribeFeatureGroupRequest = {}  # type: ignore[typeddict-item]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
