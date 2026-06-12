"""Generated from Smithy shape ``com.amazonaws.emr#InstanceTypeConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.configuration_list
    import aws_sdk_emr.types.ebs_configuration
    import aws_sdk_emr.types.instance_type
    import aws_sdk_emr.types.non_negative_double
    import aws_sdk_emr.types.whole_number
    import aws_sdk_emr.types.xml_string_max_len256


class InstanceTypeConfig(TypedDict):
    instance_type: NotRequired["aws_sdk_emr.types.instance_type.InstanceType"]
    """<p>An Amazon EC2 instance type, such as <code>m3.xlarge</code>. </p>"""
    weighted_capacity: NotRequired["aws_sdk_emr.types.whole_number.WholeNumber"]
    """<p>The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in <a>InstanceFleetConfig</a>. This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified. </p>"""
    bid_price: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The bid price for each Amazon EC2 Spot Instance type as defined by <code>InstanceType</code>. Expressed in USD. If neither <code>BidPrice</code> nor <code>BidPriceAsPercentageOfOnDemandPrice</code> is provided, <code>BidPriceAsPercentageOfOnDemandPrice</code> defaults to 100%. </p>"""
    bid_price_as_percentage_of_on_demand_price: NotRequired[
        "aws_sdk_emr.types.non_negative_double.NonNegativeDouble"
    ]
    """<p>The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by <code>InstanceType</code>. Expressed as a number (for example, 20 specifies 20%). If neither <code>BidPrice</code> nor <code>BidPriceAsPercentageOfOnDemandPrice</code> is provided, <code>BidPriceAsPercentageOfOnDemandPrice</code> defaults to 100%.</p>"""
    ebs_configuration: NotRequired[
        "aws_sdk_emr.types.ebs_configuration.EbsConfiguration"
    ]
    """<p>The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by <code>InstanceType</code>. </p>"""
    configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<p>A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software that run on the cluster.</p>"""
    custom_ami_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The custom AMI ID to use for the instance type.</p>"""
    priority: NotRequired["aws_sdk_emr.types.non_negative_double.NonNegativeDouble"]
    """<p>The priority at which Amazon EMR launches the Amazon EC2 instances with this instance type. Priority starts at 0, which is the highest priority. Amazon EMR considers the highest priority first.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceTypeConfig) -> dict:
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
    if "ebs_configuration" in value:
        import aws_sdk_emr.types.ebs_configuration

        out["EbsConfiguration"] = (
            aws_sdk_emr.types.ebs_configuration.serialize_aws_json_1_1(
                value["ebs_configuration"]
            )
        )
    if "configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["Configurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "custom_ami_id" in value:
        out["CustomAmiId"] = value["custom_ami_id"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceTypeConfig:
    out: InstanceTypeConfig = {}  # type: ignore[typeddict-item]
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
    if "EbsConfiguration" in data:
        import aws_sdk_emr.types.ebs_configuration

        out["ebs_configuration"] = (
            aws_sdk_emr.types.ebs_configuration.deserialize_aws_json_1_1(
                data["EbsConfiguration"]
            )
        )
    if "Configurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if "CustomAmiId" in data:
        out["custom_ami_id"] = data["CustomAmiId"]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    return out
