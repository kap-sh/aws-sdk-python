"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTrainingPlanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.spare_instance_count_per_ultra_server
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.training_plan_name
    import aws_sdk_sagemaker.types.training_plan_offering_id


class CreateTrainingPlanRequest(TypedDict):
    training_plan_name: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_name.TrainingPlanName"
    ]
    """<p>The name of the training plan to create.</p>"""
    training_plan_offering_id: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_offering_id.TrainingPlanOfferingId"
    ]
    """<p>The unique identifier of the training plan offering to use for creating this plan.</p>"""
    spare_instance_count_per_ultra_server: NotRequired[
        "aws_sdk_sagemaker.types.spare_instance_count_per_ultra_server.SpareInstanceCountPerUltraServer"
    ]
    """<p>Number of spare instances to reserve per UltraServer for enhanced resiliency. Default is 1.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
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
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
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
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
