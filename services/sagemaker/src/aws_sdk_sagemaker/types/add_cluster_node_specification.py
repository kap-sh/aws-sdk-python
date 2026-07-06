"""Generated from Smithy shape ``com.amazonaws.sagemaker#AddClusterNodeSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_add_increment_count
    import aws_sdk_sagemaker.types.cluster_availability_zones
    import aws_sdk_sagemaker.types.cluster_instance_group_name
    import aws_sdk_sagemaker.types.cluster_instance_types


class AddClusterNodeSpecification(TypedDict, closed=True):
    instance_group_name: (
        "aws_sdk_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    )
    """<p>The name of the instance group to which you want to add nodes.</p>"""
    increment_target_count_by: (
        "aws_sdk_sagemaker.types.batch_add_increment_count.BatchAddIncrementCount"
    )
    """<p>The number of nodes to add to the specified instance group. The total number of nodes across all instance groups in a single request cannot exceed 50.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_sagemaker.types.cluster_availability_zones.ClusterAvailabilityZones"
    ]
    """<p>The availability zones in which to add nodes. Use this to target node placement in specific availability zones within a flexible instance group.</p>"""
    instance_types: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_types.ClusterInstanceTypes"
    ]
    """<p>The instance types to use when adding nodes. Use this to target specific instance types within a flexible instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddClusterNodeSpecification) -> dict:
    out: dict = {}
    out["InstanceGroupName"] = value["instance_group_name"]
    out["IncrementTargetCountBy"] = value["increment_target_count_by"]
    if "availability_zones" in value:
        import aws_sdk_sagemaker.types.cluster_availability_zones

        out["AvailabilityZones"] = (
            aws_sdk_sagemaker.types.cluster_availability_zones.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    if "instance_types" in value:
        import aws_sdk_sagemaker.types.cluster_instance_types

        out["InstanceTypes"] = (
            aws_sdk_sagemaker.types.cluster_instance_types.serialize_aws_json_1_1(
                value["instance_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddClusterNodeSpecification:
    out: AddClusterNodeSpecification = {}  # type: ignore[typeddict-item]
    if "InstanceGroupName" in data:
        out["instance_group_name"] = data["InstanceGroupName"]
    else:
        raise DeserializationError(
            "AddClusterNodeSpecification.instance_group_name required"
        )
    if "IncrementTargetCountBy" in data:
        out["increment_target_count_by"] = data["IncrementTargetCountBy"]
    else:
        raise DeserializationError(
            "AddClusterNodeSpecification.increment_target_count_by required"
        )
    if "AvailabilityZones" in data:
        import aws_sdk_sagemaker.types.cluster_availability_zones

        out["availability_zones"] = (
            aws_sdk_sagemaker.types.cluster_availability_zones.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    if "InstanceTypes" in data:
        import aws_sdk_sagemaker.types.cluster_instance_types

        out["instance_types"] = (
            aws_sdk_sagemaker.types.cluster_instance_types.deserialize_aws_json_1_1(
                data["InstanceTypes"]
            )
        )
    return out
