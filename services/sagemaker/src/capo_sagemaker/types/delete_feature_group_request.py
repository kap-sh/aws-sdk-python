"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteFeatureGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.feature_group_name


class DeleteFeatureGroupRequest(TypedDict, closed=True):
    feature_group_name: NotRequired[
        "capo_sagemaker.types.feature_group_name.FeatureGroupName"
    ]
    """<p>The name of the <code>FeatureGroup</code> you want to delete. The name must be unique within an Amazon Web Services Region in an Amazon Web Services account. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFeatureGroupRequest) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFeatureGroupRequest:
    out: DeleteFeatureGroupRequest = {}  # type: ignore[typeddict-item]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    return out
