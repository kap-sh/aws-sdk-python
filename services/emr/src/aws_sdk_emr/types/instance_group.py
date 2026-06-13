"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.auto_scaling_policy_description
    import aws_sdk_emr.types.boolean_object
    import aws_sdk_emr.types.configuration_list
    import aws_sdk_emr.types.ebs_block_device_list
    import aws_sdk_emr.types.instance_group_id
    import aws_sdk_emr.types.instance_group_status
    import aws_sdk_emr.types.instance_group_type
    import aws_sdk_emr.types.instance_type
    import aws_sdk_emr.types.integer
    import aws_sdk_emr.types.long
    import aws_sdk_emr.types.market_type
    import aws_sdk_emr.types.shrink_policy
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.xml_string_max_len256


class InstanceGroup(TypedDict):
    id: NotRequired["aws_sdk_emr.types.instance_group_id.InstanceGroupId"]
    """<p>The identifier of the instance group.</p>"""
    name: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The name of the instance group.</p>"""
    market: NotRequired["aws_sdk_emr.types.market_type.MarketType"]
    """<p>The marketplace to provision instances for this group. Valid values are ON_DEMAND or SPOT.</p>"""
    instance_group_type: NotRequired[
        "aws_sdk_emr.types.instance_group_type.InstanceGroupType"
    ]
    """<p>The type of the instance group. Valid values are MASTER, CORE or TASK.</p>"""
    bid_price: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The bid price for each Amazon EC2 Spot Instance type as defined by <code>InstanceType</code>. Expressed in USD. If neither <code>BidPrice</code> nor <code>BidPriceAsPercentageOfOnDemandPrice</code> is provided, <code>BidPriceAsPercentageOfOnDemandPrice</code> defaults to 100%.</p>"""
    instance_type: NotRequired["aws_sdk_emr.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 instance type for all instances in the instance group.</p>"""
    requested_instance_count: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The target number of instances for the instance group.</p>"""
    running_instance_count: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The number of instances currently running in this instance group.</p>"""
    status: NotRequired["aws_sdk_emr.types.instance_group_status.InstanceGroupStatus"]
    """<p>The current status of the instance group.</p>"""
    configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<note> <p>Amazon EMR releases 4.x or later.</p> </note> <p>The list of configurations supplied for an Amazon EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).</p>"""
    configurations_version: NotRequired["aws_sdk_emr.types.long.Long"]
    """<p>The version number of the requested configuration specification for this instance group.</p>"""
    last_successfully_applied_configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<p>A list of configurations that were successfully applied for an instance group last time.</p>"""
    last_successfully_applied_configurations_version: NotRequired[
        "aws_sdk_emr.types.long.Long"
    ]
    """<p>The version number of a configuration specification that was successfully applied for an instance group last time. </p>"""
    ebs_block_devices: NotRequired[
        "aws_sdk_emr.types.ebs_block_device_list.EbsBlockDeviceList"
    ]
    """<p>The EBS block devices that are mapped to this instance group.</p>"""
    ebs_optimized: NotRequired["aws_sdk_emr.types.boolean_object.BooleanObject"]
    """<p>If the instance group is EBS-optimized. An Amazon EBS-optimized instance uses an optimized configuration stack and provides additional, dedicated capacity for Amazon EBS I/O.</p>"""
    shrink_policy: NotRequired["aws_sdk_emr.types.shrink_policy.ShrinkPolicy"]
    """<p>Policy for customizing shrink operations.</p>"""
    auto_scaling_policy: NotRequired[
        "aws_sdk_emr.types.auto_scaling_policy_description.AutoScalingPolicyDescription"
    ]
    """<p>An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates Amazon EC2 instances in response to the value of a CloudWatch metric. See PutAutoScalingPolicy.</p>"""
    custom_ami_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The custom AMI ID to use for the provisioned instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroup) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "market" in value:
        import aws_sdk_emr.types.market_type

        out["Market"] = aws_sdk_emr.types.market_type.serialize_aws_json_1_1(
            value["market"]
        )
    if "instance_group_type" in value:
        import aws_sdk_emr.types.instance_group_type

        out["InstanceGroupType"] = (
            aws_sdk_emr.types.instance_group_type.serialize_aws_json_1_1(
                value["instance_group_type"]
            )
        )
    if "bid_price" in value:
        out["BidPrice"] = value["bid_price"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "requested_instance_count" in value:
        out["RequestedInstanceCount"] = value["requested_instance_count"]
    if "running_instance_count" in value:
        out["RunningInstanceCount"] = value["running_instance_count"]
    if "status" in value:
        import aws_sdk_emr.types.instance_group_status

        out["Status"] = aws_sdk_emr.types.instance_group_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["Configurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "configurations_version" in value:
        out["ConfigurationsVersion"] = value["configurations_version"]
    if "last_successfully_applied_configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["LastSuccessfullyAppliedConfigurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["last_successfully_applied_configurations"]
            )
        )
    if "last_successfully_applied_configurations_version" in value:
        out["LastSuccessfullyAppliedConfigurationsVersion"] = value[
            "last_successfully_applied_configurations_version"
        ]
    if "ebs_block_devices" in value:
        import aws_sdk_emr.types.ebs_block_device_list

        out["EbsBlockDevices"] = (
            aws_sdk_emr.types.ebs_block_device_list.serialize_aws_json_1_1(
                value["ebs_block_devices"]
            )
        )
    if "ebs_optimized" in value:
        out["EbsOptimized"] = value["ebs_optimized"]
    if "shrink_policy" in value:
        import aws_sdk_emr.types.shrink_policy

        out["ShrinkPolicy"] = aws_sdk_emr.types.shrink_policy.serialize_aws_json_1_1(
            value["shrink_policy"]
        )
    if "auto_scaling_policy" in value:
        import aws_sdk_emr.types.auto_scaling_policy_description

        out["AutoScalingPolicy"] = (
            aws_sdk_emr.types.auto_scaling_policy_description.serialize_aws_json_1_1(
                value["auto_scaling_policy"]
            )
        )
    if "custom_ami_id" in value:
        out["CustomAmiId"] = value["custom_ami_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroup:
    out: InstanceGroup = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Market" in data:
        import aws_sdk_emr.types.market_type

        out["market"] = aws_sdk_emr.types.market_type.deserialize_aws_json_1_1(
            data["Market"]
        )
    if "InstanceGroupType" in data:
        import aws_sdk_emr.types.instance_group_type

        out["instance_group_type"] = (
            aws_sdk_emr.types.instance_group_type.deserialize_aws_json_1_1(
                data["InstanceGroupType"]
            )
        )
    if "BidPrice" in data:
        out["bid_price"] = data["BidPrice"]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "RequestedInstanceCount" in data:
        out["requested_instance_count"] = data["RequestedInstanceCount"]
    if "RunningInstanceCount" in data:
        out["running_instance_count"] = data["RunningInstanceCount"]
    if "Status" in data:
        import aws_sdk_emr.types.instance_group_status

        out["status"] = (
            aws_sdk_emr.types.instance_group_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Configurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if "ConfigurationsVersion" in data:
        out["configurations_version"] = data["ConfigurationsVersion"]
    if "LastSuccessfullyAppliedConfigurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["last_successfully_applied_configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["LastSuccessfullyAppliedConfigurations"]
            )
        )
    if "LastSuccessfullyAppliedConfigurationsVersion" in data:
        out["last_successfully_applied_configurations_version"] = data[
            "LastSuccessfullyAppliedConfigurationsVersion"
        ]
    if "EbsBlockDevices" in data:
        import aws_sdk_emr.types.ebs_block_device_list

        out["ebs_block_devices"] = (
            aws_sdk_emr.types.ebs_block_device_list.deserialize_aws_json_1_1(
                data["EbsBlockDevices"]
            )
        )
    if "EbsOptimized" in data:
        out["ebs_optimized"] = data["EbsOptimized"]
    if "ShrinkPolicy" in data:
        import aws_sdk_emr.types.shrink_policy

        out["shrink_policy"] = aws_sdk_emr.types.shrink_policy.deserialize_aws_json_1_1(
            data["ShrinkPolicy"]
        )
    if "AutoScalingPolicy" in data:
        import aws_sdk_emr.types.auto_scaling_policy_description

        out["auto_scaling_policy"] = (
            aws_sdk_emr.types.auto_scaling_policy_description.deserialize_aws_json_1_1(
                data["AutoScalingPolicy"]
            )
        )
    if "CustomAmiId" in data:
        out["custom_ami_id"] = data["CustomAmiId"]
    return out
