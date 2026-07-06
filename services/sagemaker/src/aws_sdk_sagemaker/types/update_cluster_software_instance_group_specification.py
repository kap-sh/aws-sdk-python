"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateClusterSoftwareInstanceGroupSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_group_name


class UpdateClusterSoftwareInstanceGroupSpecification(TypedDict, closed=True):
    instance_group_name: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>The name of the instance group to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateClusterSoftwareInstanceGroupSpecification,
) -> dict:
    out: dict = {}
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateClusterSoftwareInstanceGroupSpecification:
    out: UpdateClusterSoftwareInstanceGroupSpecification = {}  # type: ignore[typeddict-item]
    if "InstanceGroupName" in data:
        out["instance_group_name"] = data["InstanceGroupName"]
    return out
