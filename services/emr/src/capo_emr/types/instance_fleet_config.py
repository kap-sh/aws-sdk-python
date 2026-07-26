"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.instance_fleet_provisioning_specifications
    import capo_emr.types.instance_fleet_resizing_specifications
    import capo_emr.types.instance_fleet_type
    import capo_emr.types.instance_type_config_list
    import capo_emr.types.whole_number
    import capo_emr.types.xml_string_max_len256


class InstanceFleetConfig(TypedDict, closed=True):
    name: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The friendly name of the instance fleet.</p>"""
    instance_fleet_type: NotRequired[
        "capo_emr.types.instance_fleet_type.InstanceFleetType"
    ]
    """<p>The node type that the instance fleet hosts. Valid values are MASTER, CORE, and TASK.</p>"""
    target_on_demand_capacity: NotRequired["capo_emr.types.whole_number.WholeNumber"]
    """<p>The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand Instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand Instances as specified by <a>InstanceTypeConfig</a>. Each instance configuration has a specified <code>WeightedCapacity</code>. When an On-Demand Instance is provisioned, the <code>WeightedCapacity</code> units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a <code>WeightedCapacity</code> of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.</p> <note> <p>If not specified or set to 0, only Spot Instances are provisioned for the instance fleet using <code>TargetSpotCapacity</code>. At least one of <code>TargetSpotCapacity</code> and <code>TargetOnDemandCapacity</code> should be greater than 0. For a master instance fleet, only one of <code>TargetSpotCapacity</code> and <code>TargetOnDemandCapacity</code> can be specified, and its value must be 1.</p> </note>"""
    target_spot_capacity: NotRequired["capo_emr.types.whole_number.WholeNumber"]
    """<p>The target capacity of Spot units for the instance fleet, which determines how many Spot Instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot Instances as specified by <a>InstanceTypeConfig</a>. Each instance configuration has a specified <code>WeightedCapacity</code>. When a Spot Instance is provisioned, the <code>WeightedCapacity</code> units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a <code>WeightedCapacity</code> of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.</p> <note> <p>If not specified or set to 0, only On-Demand Instances are provisioned for the instance fleet. At least one of <code>TargetSpotCapacity</code> and <code>TargetOnDemandCapacity</code> should be greater than 0. For a master instance fleet, only one of <code>TargetSpotCapacity</code> and <code>TargetOnDemandCapacity</code> can be specified, and its value must be 1.</p> </note>"""
    instance_type_configs: NotRequired[
        "capo_emr.types.instance_type_config_list.InstanceTypeConfigList"
    ]
    """<p>The instance type configurations that define the Amazon EC2 instances in the instance fleet.</p>"""
    launch_specifications: NotRequired[
        "capo_emr.types.instance_fleet_provisioning_specifications.InstanceFleetProvisioningSpecifications"
    ]
    """<p>The launch specification for the instance fleet.</p>"""
    resize_specifications: NotRequired[
        "capo_emr.types.instance_fleet_resizing_specifications.InstanceFleetResizingSpecifications"
    ]
    """<p>The resize specification for the instance fleet.</p>"""
    context: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>Reserved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetConfig) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "instance_fleet_type" in value:
        import capo_emr.types.instance_fleet_type

        out["InstanceFleetType"] = (
            capo_emr.types.instance_fleet_type.serialize_aws_json_1_1(
                value["instance_fleet_type"]
            )
        )
    if "target_on_demand_capacity" in value:
        out["TargetOnDemandCapacity"] = value["target_on_demand_capacity"]
    if "target_spot_capacity" in value:
        out["TargetSpotCapacity"] = value["target_spot_capacity"]
    if "instance_type_configs" in value:
        import capo_emr.types.instance_type_config_list

        out["InstanceTypeConfigs"] = (
            capo_emr.types.instance_type_config_list.serialize_aws_json_1_1(
                value["instance_type_configs"]
            )
        )
    if "launch_specifications" in value:
        import capo_emr.types.instance_fleet_provisioning_specifications

        out["LaunchSpecifications"] = (
            capo_emr.types.instance_fleet_provisioning_specifications.serialize_aws_json_1_1(
                value["launch_specifications"]
            )
        )
    if "resize_specifications" in value:
        import capo_emr.types.instance_fleet_resizing_specifications

        out["ResizeSpecifications"] = (
            capo_emr.types.instance_fleet_resizing_specifications.serialize_aws_json_1_1(
                value["resize_specifications"]
            )
        )
    if "context" in value:
        out["Context"] = value["context"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceFleetConfig:
    out: InstanceFleetConfig = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "InstanceFleetType" in data:
        import capo_emr.types.instance_fleet_type

        out["instance_fleet_type"] = (
            capo_emr.types.instance_fleet_type.deserialize_aws_json_1_1(
                data["InstanceFleetType"]
            )
        )
    if "TargetOnDemandCapacity" in data:
        out["target_on_demand_capacity"] = data["TargetOnDemandCapacity"]
    if "TargetSpotCapacity" in data:
        out["target_spot_capacity"] = data["TargetSpotCapacity"]
    if "InstanceTypeConfigs" in data:
        import capo_emr.types.instance_type_config_list

        out["instance_type_configs"] = (
            capo_emr.types.instance_type_config_list.deserialize_aws_json_1_1(
                data["InstanceTypeConfigs"]
            )
        )
    if "LaunchSpecifications" in data:
        import capo_emr.types.instance_fleet_provisioning_specifications

        out["launch_specifications"] = (
            capo_emr.types.instance_fleet_provisioning_specifications.deserialize_aws_json_1_1(
                data["LaunchSpecifications"]
            )
        )
    if "ResizeSpecifications" in data:
        import capo_emr.types.instance_fleet_resizing_specifications

        out["resize_specifications"] = (
            capo_emr.types.instance_fleet_resizing_specifications.deserialize_aws_json_1_1(
                data["ResizeSpecifications"]
            )
        )
    if "Context" in data:
        out["context"] = data["Context"]
    return out
