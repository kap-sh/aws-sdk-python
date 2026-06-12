"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleet``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_fleet_id
    import aws_sdk_emr.types.instance_fleet_provisioning_specifications
    import aws_sdk_emr.types.instance_fleet_resizing_specifications
    import aws_sdk_emr.types.instance_fleet_status
    import aws_sdk_emr.types.instance_fleet_type
    import aws_sdk_emr.types.instance_type_specification_list
    import aws_sdk_emr.types.whole_number
    import aws_sdk_emr.types.xml_string_max_len256


class InstanceFleet(TypedDict):
    id: NotRequired["aws_sdk_emr.types.instance_fleet_id.InstanceFleetId"]
    """<p>The unique identifier of the instance fleet.</p>"""
    name: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>A friendly name for the instance fleet.</p>"""
    status: NotRequired["aws_sdk_emr.types.instance_fleet_status.InstanceFleetStatus"]
    """<p>The current status of the instance fleet. </p>"""
    instance_fleet_type: NotRequired[
        "aws_sdk_emr.types.instance_fleet_type.InstanceFleetType"
    ]
    """<p>The node type that the instance fleet hosts. Valid values are MASTER, CORE, or TASK. </p>"""
    target_on_demand_capacity: NotRequired["aws_sdk_emr.types.whole_number.WholeNumber"]
    """<p>The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand Instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand Instances as specified by <a>InstanceTypeConfig</a>. Each instance configuration has a specified <code>WeightedCapacity</code>. When an On-Demand Instance is provisioned, the <code>WeightedCapacity</code> units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a <code>WeightedCapacity</code> of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. You can use <a>InstanceFleet$ProvisionedOnDemandCapacity</a> to determine the Spot capacity units that have been provisioned for the instance fleet.</p> <note> <p>If not specified or set to 0, only Spot Instances are provisioned for the instance fleet using <code>TargetSpotCapacity</code>. At least one of <code>TargetSpotCapacity</code> and <code>TargetOnDemandCapacity</code> should be greater than 0. For a master instance fleet, only one of <code>TargetSpotCapacity</code> and <code>TargetOnDemandCapacity</code> can be specified, and its value must be 1.</p> </note>"""
    target_spot_capacity: NotRequired["aws_sdk_emr.types.whole_number.WholeNumber"]
    """<p>The target capacity of Spot units for the instance fleet, which determines how many Spot Instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot Instances as specified by <a>InstanceTypeConfig</a>. Each instance configuration has a specified <code>WeightedCapacity</code>. When a Spot instance is provisioned, the <code>WeightedCapacity</code> units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a <code>WeightedCapacity</code> of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. You can use <a>InstanceFleet$ProvisionedSpotCapacity</a> to determine the Spot capacity units that have been provisioned for the instance fleet.</p> <note> <p>If not specified or set to 0, only On-Demand Instances are provisioned for the instance fleet. At least one of <code>TargetSpotCapacity</code> and <code>TargetOnDemandCapacity</code> should be greater than 0. For a master instance fleet, only one of <code>TargetSpotCapacity</code> and <code>TargetOnDemandCapacity</code> can be specified, and its value must be 1.</p> </note>"""
    provisioned_on_demand_capacity: NotRequired[
        "aws_sdk_emr.types.whole_number.WholeNumber"
    ]
    """<p>The number of On-Demand units that have been provisioned for the instance fleet to fulfill <code>TargetOnDemandCapacity</code>. This provisioned capacity might be less than or greater than <code>TargetOnDemandCapacity</code>.</p>"""
    provisioned_spot_capacity: NotRequired["aws_sdk_emr.types.whole_number.WholeNumber"]
    """<p>The number of Spot units that have been provisioned for this instance fleet to fulfill <code>TargetSpotCapacity</code>. This provisioned capacity might be less than or greater than <code>TargetSpotCapacity</code>.</p>"""
    instance_type_specifications: NotRequired[
        "aws_sdk_emr.types.instance_type_specification_list.InstanceTypeSpecificationList"
    ]
    """<p>An array of specifications for the instance types that comprise an instance fleet.</p>"""
    launch_specifications: NotRequired[
        "aws_sdk_emr.types.instance_fleet_provisioning_specifications.InstanceFleetProvisioningSpecifications"
    ]
    """<p>Describes the launch specification for an instance fleet. </p>"""
    resize_specifications: NotRequired[
        "aws_sdk_emr.types.instance_fleet_resizing_specifications.InstanceFleetResizingSpecifications"
    ]
    """<p>The resize specification for the instance fleet.</p>"""
    context: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>Reserved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleet) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_emr.types.instance_fleet_status

        out["Status"] = aws_sdk_emr.types.instance_fleet_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "instance_fleet_type" in value:
        import aws_sdk_emr.types.instance_fleet_type

        out["InstanceFleetType"] = (
            aws_sdk_emr.types.instance_fleet_type.serialize_aws_json_1_1(
                value["instance_fleet_type"]
            )
        )
    if "target_on_demand_capacity" in value:
        out["TargetOnDemandCapacity"] = value["target_on_demand_capacity"]
    if "target_spot_capacity" in value:
        out["TargetSpotCapacity"] = value["target_spot_capacity"]
    if "provisioned_on_demand_capacity" in value:
        out["ProvisionedOnDemandCapacity"] = value["provisioned_on_demand_capacity"]
    if "provisioned_spot_capacity" in value:
        out["ProvisionedSpotCapacity"] = value["provisioned_spot_capacity"]
    if "instance_type_specifications" in value:
        import aws_sdk_emr.types.instance_type_specification_list

        out["InstanceTypeSpecifications"] = (
            aws_sdk_emr.types.instance_type_specification_list.serialize_aws_json_1_1(
                value["instance_type_specifications"]
            )
        )
    if "launch_specifications" in value:
        import aws_sdk_emr.types.instance_fleet_provisioning_specifications

        out["LaunchSpecifications"] = (
            aws_sdk_emr.types.instance_fleet_provisioning_specifications.serialize_aws_json_1_1(
                value["launch_specifications"]
            )
        )
    if "resize_specifications" in value:
        import aws_sdk_emr.types.instance_fleet_resizing_specifications

        out["ResizeSpecifications"] = (
            aws_sdk_emr.types.instance_fleet_resizing_specifications.serialize_aws_json_1_1(
                value["resize_specifications"]
            )
        )
    if "context" in value:
        out["Context"] = value["context"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceFleet:
    out: InstanceFleet = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_emr.types.instance_fleet_status

        out["status"] = (
            aws_sdk_emr.types.instance_fleet_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "InstanceFleetType" in data:
        import aws_sdk_emr.types.instance_fleet_type

        out["instance_fleet_type"] = (
            aws_sdk_emr.types.instance_fleet_type.deserialize_aws_json_1_1(
                data["InstanceFleetType"]
            )
        )
    if "TargetOnDemandCapacity" in data:
        out["target_on_demand_capacity"] = data["TargetOnDemandCapacity"]
    if "TargetSpotCapacity" in data:
        out["target_spot_capacity"] = data["TargetSpotCapacity"]
    if "ProvisionedOnDemandCapacity" in data:
        out["provisioned_on_demand_capacity"] = data["ProvisionedOnDemandCapacity"]
    if "ProvisionedSpotCapacity" in data:
        out["provisioned_spot_capacity"] = data["ProvisionedSpotCapacity"]
    if "InstanceTypeSpecifications" in data:
        import aws_sdk_emr.types.instance_type_specification_list

        out["instance_type_specifications"] = (
            aws_sdk_emr.types.instance_type_specification_list.deserialize_aws_json_1_1(
                data["InstanceTypeSpecifications"]
            )
        )
    if "LaunchSpecifications" in data:
        import aws_sdk_emr.types.instance_fleet_provisioning_specifications

        out["launch_specifications"] = (
            aws_sdk_emr.types.instance_fleet_provisioning_specifications.deserialize_aws_json_1_1(
                data["LaunchSpecifications"]
            )
        )
    if "ResizeSpecifications" in data:
        import aws_sdk_emr.types.instance_fleet_resizing_specifications

        out["resize_specifications"] = (
            aws_sdk_emr.types.instance_fleet_resizing_specifications.deserialize_aws_json_1_1(
                data["ResizeSpecifications"]
            )
        )
    if "Context" in data:
        out["context"] = data["Context"]
    return out
