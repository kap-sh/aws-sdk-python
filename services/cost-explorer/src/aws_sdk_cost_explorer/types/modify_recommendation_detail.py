"""Generated from Smithy shape ``com.amazonaws.costexplorer#ModifyRecommendationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.target_instances_list


class ModifyRecommendationDetail(TypedDict, closed=True):
    target_instances: NotRequired[
        "aws_sdk_cost_explorer.types.target_instances_list.TargetInstancesList"
    ]
    """<p>Determines whether this instance type is the Amazon Web Services default recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyRecommendationDetail) -> dict:
    out: dict = {}
    if "target_instances" in value:
        import aws_sdk_cost_explorer.types.target_instances_list

        out["TargetInstances"] = (
            aws_sdk_cost_explorer.types.target_instances_list.serialize_aws_json_1_1(
                value["target_instances"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyRecommendationDetail:
    out: ModifyRecommendationDetail = {}  # type: ignore[typeddict-item]
    if "TargetInstances" in data:
        import aws_sdk_cost_explorer.types.target_instances_list

        out["target_instances"] = (
            aws_sdk_cost_explorer.types.target_instances_list.deserialize_aws_json_1_1(
                data["TargetInstances"]
            )
        )
    return out
