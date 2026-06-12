"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.instance_group_name
    import aws_sdk_sagemaker.types.training_instance_count
    import aws_sdk_sagemaker.types.training_instance_type


class InstanceGroup(TypedDict):
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.training_instance_type.TrainingInstanceType"
    ]
    """<p>Specifies the instance type of the instance group.</p>"""
    instance_count: NotRequired[
        "aws_sdk_sagemaker.types.training_instance_count.TrainingInstanceCount"
    ]
    """<p>Specifies the number of instances of the instance group.</p>"""
    instance_group_name: NotRequired[
        "aws_sdk_sagemaker.types.instance_group_name.InstanceGroupName"
    ]
    """<p>Specifies the name of the instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroup) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.training_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.training_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroup:
    out: InstanceGroup = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.training_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.training_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "InstanceGroupName" in data:
        out["instance_group_name"] = data["InstanceGroupName"]
    return out
