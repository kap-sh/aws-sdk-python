"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTrainingPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.spare_instance_count_per_ultra_server
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.training_plan_name
    import capo_sagemaker.types.training_plan_offering_id


class CreateTrainingPlanRequest(TypedDict, closed=True):
    training_plan_name: NotRequired[
        "capo_sagemaker.types.training_plan_name.TrainingPlanName"
    ]
    """<p>The name of the training plan to create.</p>"""
    training_plan_offering_id: NotRequired[
        "capo_sagemaker.types.training_plan_offering_id.TrainingPlanOfferingId"
    ]
    """<p>The unique identifier of the training plan offering to use for creating this plan.</p>"""
    spare_instance_count_per_ultra_server: NotRequired[
        "capo_sagemaker.types.spare_instance_count_per_ultra_server.SpareInstanceCountPerUltraServer"
    ]
    """<p>Number of spare instances to reserve per UltraServer for enhanced resiliency. Default is 1.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs to apply to this training plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrainingPlanRequest) -> dict:
    out: dict = {}
    if "training_plan_name" in value:
        out["TrainingPlanName"] = value["training_plan_name"]
    if "training_plan_offering_id" in value:
        out["TrainingPlanOfferingId"] = value["training_plan_offering_id"]
    if "spare_instance_count_per_ultra_server" in value:
        out["SpareInstanceCountPerUltraServer"] = value[
            "spare_instance_count_per_ultra_server"
        ]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrainingPlanRequest:
    out: CreateTrainingPlanRequest = {}  # type: ignore[typeddict-item]
    if "TrainingPlanName" in data:
        out["training_plan_name"] = data["TrainingPlanName"]
    if "TrainingPlanOfferingId" in data:
        out["training_plan_offering_id"] = data["TrainingPlanOfferingId"]
    if "SpareInstanceCountPerUltraServer" in data:
        out["spare_instance_count_per_ultra_server"] = data[
            "SpareInstanceCountPerUltraServer"
        ]
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
