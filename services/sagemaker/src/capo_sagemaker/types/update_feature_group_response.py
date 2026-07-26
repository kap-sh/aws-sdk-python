"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateFeatureGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.feature_group_arn


class UpdateFeatureGroupResponse(TypedDict, closed=True):
    feature_group_arn: NotRequired[
        "capo_sagemaker.types.feature_group_arn.FeatureGroupArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the feature group that you're updating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFeatureGroupResponse) -> dict:
    out: dict = {}
    if "feature_group_arn" in value:
        out["FeatureGroupArn"] = value["feature_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFeatureGroupResponse:
    out: UpdateFeatureGroupResponse = {}  # type: ignore[typeddict-item]
    if "FeatureGroupArn" in data:
        out["feature_group_arn"] = data["FeatureGroupArn"]
    return out
