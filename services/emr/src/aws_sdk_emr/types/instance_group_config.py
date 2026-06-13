"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.auto_scaling_policy
    import aws_sdk_emr.types.configuration_list
    import aws_sdk_emr.types.ebs_configuration
    import aws_sdk_emr.types.instance_role_type
    import aws_sdk_emr.types.instance_type
    import aws_sdk_emr.types.integer
    import aws_sdk_emr.types.market_type
    import aws_sdk_emr.types.xml_string_max_len256


class InstanceGroupConfig(TypedDict):
    name: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>Friendly name given to the instance group.</p>"""
    market: NotRequired["aws_sdk_emr.types.market_type.MarketType"]
    """<p>Market type of the Amazon EC2 instances used to create a cluster node.</p>"""
    instance_role: NotRequired["aws_sdk_emr.types.instance_role_type.InstanceRoleType"]
    """<p>The role of the instance group in the cluster.</p>"""
    bid_price: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The bid price for each Amazon EC2 Spot Instance type as defined by <code>InstanceType</code>. Expressed in USD. If neither <code>BidPrice</code> nor <code>BidPriceAsPercentageOfOnDemandPrice</code> is provided, <code>BidPriceAsPercentageOfOnDemandPrice</code> defaults to 100%.</p>"""
    instance_type: NotRequired["aws_sdk_emr.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 instance type for all instances in the instance group.</p>"""
    instance_count: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>Target number of instances for the instance group.</p>"""
    configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<note> <p>Amazon EMR releases 4.x or later.</p> </note> <p>The list of configurations supplied for an Amazon EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).</p>"""
    ebs_configuration: NotRequired[
        "aws_sdk_emr.types.ebs_configuration.EbsConfiguration"
    ]
    """<p>EBS configurations that will be attached to each Amazon EC2 instance in the instance group.</p>"""
    auto_scaling_policy: NotRequired[
        "aws_sdk_emr.types.auto_scaling_policy.AutoScalingPolicy"
    ]
    """<p>An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates Amazon EC2 instances in response to the value of a CloudWatch metric. See <a>PutAutoScalingPolicy</a>.</p>"""
    custom_ami_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The custom AMI ID to use for the provisioned instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupConfig) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "market" in value:
        import aws_sdk_emr.types.market_type

        out["Market"] = aws_sdk_emr.types.market_type.serialize_aws_json_1_1(
            value["market"]
        )
    if "instance_role" in value:
        import aws_sdk_emr.types.instance_role_type

        out["InstanceRole"] = (
            aws_sdk_emr.types.instance_role_type.serialize_aws_json_1_1(
                value["instance_role"]
            )
        )
    if "bid_price" in value:
        out["BidPrice"] = value["bid_price"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["Configurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "ebs_configuration" in value:
        import aws_sdk_emr.types.ebs_configuration

        out["EbsConfiguration"] = (
            aws_sdk_emr.types.ebs_configuration.serialize_aws_json_1_1(
                value["ebs_configuration"]
            )
        )
    if "auto_scaling_policy" in value:
        import aws_sdk_emr.types.auto_scaling_policy

        out["AutoScalingPolicy"] = (
            aws_sdk_emr.types.auto_scaling_policy.serialize_aws_json_1_1(
                value["auto_scaling_policy"]
            )
        )
    if "custom_ami_id" in value:
        out["CustomAmiId"] = value["custom_ami_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroupConfig:
    out: InstanceGroupConfig = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Market" in data:
        import aws_sdk_emr.types.market_type

        out["market"] = aws_sdk_emr.types.market_type.deserialize_aws_json_1_1(
            data["Market"]
        )
    if "InstanceRole" in data:
        import aws_sdk_emr.types.instance_role_type

        out["instance_role"] = (
            aws_sdk_emr.types.instance_role_type.deserialize_aws_json_1_1(
                data["InstanceRole"]
            )
        )
    if "BidPrice" in data:
        out["bid_price"] = data["BidPrice"]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "Configurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if "EbsConfiguration" in data:
        import aws_sdk_emr.types.ebs_configuration

        out["ebs_configuration"] = (
            aws_sdk_emr.types.ebs_configuration.deserialize_aws_json_1_1(
                data["EbsConfiguration"]
            )
        )
    if "AutoScalingPolicy" in data:
        import aws_sdk_emr.types.auto_scaling_policy

        out["auto_scaling_policy"] = (
            aws_sdk_emr.types.auto_scaling_policy.deserialize_aws_json_1_1(
                data["AutoScalingPolicy"]
            )
        )
    if "CustomAmiId" in data:
        out["custom_ami_id"] = data["CustomAmiId"]
    return out
