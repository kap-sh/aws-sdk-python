"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateFeatureGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_group_arn


class CreateFeatureGroupResponse(TypedDict):
    feature_group_arn: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_arn.FeatureGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the <code>FeatureGroup</code>. This is a unique identifier for the feature group. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFeatureGroupResponse) -> dict:
    out: dict = {}
    if "feature_group_arn" in value:
        out["FeatureGroupArn"] = value["feature_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFeatureGroupResponse:
    out: CreateFeatureGroupResponse = {}  # type: ignore[typeddict-item]
    if "FeatureGroupArn" in data:
        out["feature_group_arn"] = data["FeatureGroupArn"]
    return out
