"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceLaunchSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_values
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.placement
    import aws_sdk_ec2.types.security_group_id_string_list
    import aws_sdk_ec2.types.security_group_string_list
    import aws_sdk_ec2.types.shutdown_behavior
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.user_data


class ImportInstanceLaunchSpecification(TypedDict):
    architecture: NotRequired[
        "aws_sdk_ec2.types.architecture_values.ArchitectureValues"
    ]
    """<p>The architecture of the instance.</p>"""
    group_names: NotRequired[
        "aws_sdk_ec2.types.security_group_string_list.SecurityGroupStringList"
    ]
    """<p>The security group names.</p>"""
    group_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The security group IDs.</p>"""
    additional_info: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    user_data: NotRequired["aws_sdk_ec2.types.user_data.UserData"]
    """<p>The Base64-encoded user data to make available to the instance.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. For more information about the instance types that you can import, see <a href=\"https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#vmimport-instance-types\">Instance Types</a> in the VM Import/Export User Guide.</p>"""
    placement: NotRequired["aws_sdk_ec2.types.placement.Placement"]
    """<p>The placement information for the instance.</p>"""
    monitoring: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether monitoring is enabled.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>[EC2-VPC] The ID of the subnet in which to launch the instance.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "aws_sdk_ec2.types.shutdown_behavior.ShutdownBehavior"
    ]
    """<p>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>[EC2-VPC] An available IP address from the IP address range of the subnet.</p>"""
