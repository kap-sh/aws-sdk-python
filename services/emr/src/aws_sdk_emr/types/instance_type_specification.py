"""Generated from Smithy shape ``com.amazonaws.emr#InstanceTypeSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean_object
    import aws_sdk_emr.types.configuration_list
    import aws_sdk_emr.types.ebs_block_device_list
    import aws_sdk_emr.types.instance_type
    import aws_sdk_emr.types.non_negative_double
    import aws_sdk_emr.types.whole_number
    import aws_sdk_emr.types.xml_string_max_len256


class InstanceTypeSpecification(TypedDict):
    instance_type: NotRequired["aws_sdk_emr.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 instance type, for example <code>m3.xlarge</code>.</p>"""
    weighted_capacity: NotRequired["aws_sdk_emr.types.whole_number.WholeNumber"]
    """<p>The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in <a>InstanceFleetConfig</a>. Capacity values represent performance characteristics such as vCPUs, memory, or I/O. If not specified, the default value is 1.</p>"""
    bid_price: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The bid price for each Amazon EC2 Spot Instance type as defined by <code>InstanceType</code>. Expressed in USD. If neither <code>BidPrice</code> nor <code>BidPriceAsPercentageOfOnDemandPrice</code> is provided, <code>BidPriceAsPercentageOfOnDemandPrice</code> defaults to 100%.</p>"""
    bid_price_as_percentage_of_on_demand_price: NotRequired[
        "aws_sdk_emr.types.non_negative_double.NonNegativeDouble"
    ]
    """<p>The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by <code>InstanceType</code>. Expressed as a number (for example, 20 specifies 20%).</p>"""
    configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<p>A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR.</p>"""
    ebs_block_devices: NotRequired[
        "aws_sdk_emr.types.ebs_block_device_list.EbsBlockDeviceList"
    ]
    """<p>The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by <code>InstanceType</code>.</p>"""
    ebs_optimized: NotRequired["aws_sdk_emr.types.boolean_object.BooleanObject"]
    """<p>Evaluates to <code>TRUE</code> when the specified <code>InstanceType</code> is EBS-optimized.</p>"""
    custom_ami_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The custom AMI ID to use for the instance type.</p>"""
    priority: NotRequired["aws_sdk_emr.types.non_negative_double.NonNegativeDouble"]
    """<p>The priority at which Amazon EMR launches the Amazon EC2 instances with this instance type. Priority starts at 0, which is the highest priority. Amazon EMR considers the highest priority first.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceTypeSpecification) -> dict:
    out: dict = {}
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "weighted_capacity" in value:
        out["WeightedCapacity"] = value["weighted_capacity"]
    if "bid_price" in value:
        out["BidPrice"] = value["bid_price"]
    if "bid_price_as_percentage_of_on_demand_price" in value:
        out["BidPriceAsPercentageOfOnDemandPrice"] = value[
            "bid_price_as_percentage_of_on_demand_price"
        ]
    if "configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["Configurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "ebs_block_devices" in value:
        import aws_sdk_emr.types.ebs_block_device_list

        out["EbsBlockDevices"] = (
            aws_sdk_emr.types.ebs_block_device_list.serialize_aws_json_1_1(
                value["ebs_block_devices"]
            )
        )
    if "ebs_optimized" in value:
        out["EbsOptimized"] = value["ebs_optimized"]
    if "custom_ami_id" in value:
        out["CustomAmiId"] = value["custom_ami_id"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceTypeSpecification:
    out: InstanceTypeSpecification = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "WeightedCapacity" in data:
        out["weighted_capacity"] = data["WeightedCapacity"]
    if "BidPrice" in data:
        out["bid_price"] = data["BidPrice"]
    if "BidPriceAsPercentageOfOnDemandPrice" in data:
        out["bid_price_as_percentage_of_on_demand_price"] = data[
            "BidPriceAsPercentageOfOnDemandPrice"
        ]
    if "Configurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if "EbsBlockDevices" in data:
        import aws_sdk_emr.types.ebs_block_device_list

        out["ebs_block_devices"] = (
            aws_sdk_emr.types.ebs_block_device_list.deserialize_aws_json_1_1(
                data["EbsBlockDevices"]
            )
        )
    if "EbsOptimized" in data:
        out["ebs_optimized"] = data["EbsOptimized"]
    if "CustomAmiId" in data:
        out["custom_ami_id"] = data["CustomAmiId"]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    return out
