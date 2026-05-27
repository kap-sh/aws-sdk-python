"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateOverrides``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.block_device_mapping_response_list
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.instance_requirements
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.placement_response
    import aws_sdk_ec2.types.string


class FleetLaunchTemplateOverrides(TypedDict):
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p> <p> <code>mac1.metal</code> is not supported as a launch template override.</p> <note> <p>If you specify <code>InstanceType</code>, you can't specify <code>InstanceRequirements</code>.</p> </note>"""
    max_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price. </p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> <p>If you specify a maximum price, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an <code>InvalidParameterValue</code> error message.</p> </important>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet in which to launch the instances.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone in which to launch the instances. For example, <code>us-east-2a</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    weighted_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms of instances, or a performance characteristic such as vCPUs, memory, or I/O.</p> <p>If the target capacity divided by this value is not a whole number, Amazon EC2 rounds the number of instances to the next whole number. If this value is not specified, the default is 1.</p> <note> <p>When specifying weights, the price used in the <code>lowest-price</code> and <code>price-capacity-optimized</code> allocation strategies is per <i>unit</i> hour (where the instance price is divided by the specified weight). However, if all the specified weights are above the requested <code>TargetCapacity</code>, resulting in only 1 instance being launched, the price used is per <i>instance</i> hour.</p> </note>"""
    priority: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The priority for the launch template override. The highest priority is launched first.</p> <p>If the On-Demand <code>AllocationStrategy</code> is set to <code>prioritized</code>, EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity.</p> <p>If the Spot <code>AllocationStrategy</code> is set to <code>capacity-optimized-prioritized</code>, EC2 Fleet uses priority on a best-effort basis to determine which launch template override to use in fulfilling Spot capacity, but optimizes for capacity first.</p> <p>Valid values are whole numbers starting at <code>0</code>. The lower the number, the higher the priority. If no number is set, the override has the lowest priority. You can set the same priority for different launch template overrides.</p>"""
    placement: NotRequired["aws_sdk_ec2.types.placement_response.PlacementResponse"]
    """<p>The location where the instance launched, if applicable.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_ec2.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.</p> <note> <p>If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceType</code>.</p> </note>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI in the format <code>ami-17characters00000</code>.</p> <p>Alternatively, you can specify a Systems Manager parameter, using one of the following formats. The Systems Manager parameter will resolve to an AMI ID on launch.</p> <p>To reference a public parameter:</p> <ul> <li> <p> <code>resolve:ssm:<i>public-parameter</i> </code> </p> </li> </ul> <p>To reference a parameter stored in the same account:</p> <ul> <li> <p> <code>resolve:ssm:<i>parameter-name</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-name:version-number</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-name:label</i> </code> </p> </li> </ul> <p>To reference a parameter shared from another Amazon Web Services account:</p> <ul> <li> <p> <code>resolve:ssm:<i>parameter-ARN</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-ARN:version-number</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-ARN:label</i> </code> </p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id\">Use a Systems Manager parameter instead of an AMI ID</a> in the <i>Amazon EC2 User Guide</i>.</p> <note> <p>This parameter is only available for fleets of type <code>instant</code>. For fleets of type <code>maintain</code> and <code>request</code>, you must specify the AMI ID in the launch template.</p> </note>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.block_device_mapping_response_list.BlockDeviceMappingResponseList"
    ]
    """<p>The block device mappings, which define the EBS volumes and instance store volumes to attach to the instance at launch.</p> <p>Supported only for fleets of type <code>instant</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html\">Block device mappings for volumes on Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone in which to launch the instances. For example, <code>use2-az1</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
