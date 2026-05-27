"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_boolean_value
    import aws_sdk_ec2.types.attribute_value
    import aws_sdk_ec2.types.blob_attribute_value
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.enclave_options_request
    import aws_sdk_ec2.types.group_id_string_list
    import aws_sdk_ec2.types.instance_attribute_name
    import aws_sdk_ec2.types.instance_block_device_mapping_specification_list
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.modify_instance_attribute_value


class ModifyInstanceAttributeRequest(TypedDict):
    source_dest_check: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of any traffic that it receives. If the value is <code>true</code>, source/destination checks are enabled; otherwise, they are disabled. The default value is <code>true</code>. You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls.</p>"""
    enclave_options: NotRequired[
        "aws_sdk_ec2.types.enclave_options_request.EnclaveOptionsRequest"
    ]
    """<p>Enables or disables the instance for Amazon Web Services Nitro Enclaves. For more information, see the <a href=\"https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html\">Amazon Web Services Nitro Enclaves User Guide</a>.</p>"""
    disable_api_stop: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether an instance is enabled for stop protection. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html\">Enable stop protection for your instance</a>.</p> <p></p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    attribute: NotRequired[
        "aws_sdk_ec2.types.instance_attribute_name.InstanceAttributeName"
    ]
    """<p>The name of the attribute to modify.</p> <note> <p>When changing the instance type: If the original instance type is configured for configurable bandwidth, and the desired instance type doesn't support configurable bandwidth, first set the existing bandwidth configuration to <code>default</code> using the <a>ModifyInstanceNetworkPerformanceOptions</a> operation.</p> </note> <important> <p>You can modify the following attributes only: <code>disableApiTermination</code> | <code>instanceType</code> | <code>kernel</code> | <code>ramdisk</code> | <code>instanceInitiatedShutdownBehavior</code> | <code>blockDeviceMapping</code> | <code>userData</code> | <code>sourceDestCheck</code> | <code>groupSet</code> | <code>ebsOptimized</code> | <code>sriovNetSupport</code> | <code>enaSupport</code> | <code>nvmeSupport</code> | <code>disableApiStop</code> | <code>enclaveOptions</code> </p> </important>"""
    value: NotRequired[
        "aws_sdk_ec2.types.modify_instance_attribute_value.ModifyInstanceAttributeValue"
    ]
    """<p>A new value for the attribute. Use only with the <code>kernel</code>, <code>ramdisk</code>, <code>userData</code>, <code>disableApiTermination</code>, or <code>instanceInitiatedShutdownBehavior</code> attribute.</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.instance_block_device_mapping_specification_list.InstanceBlockDeviceMappingSpecificationList"
    ]
    """<p>Modifies the <code>DeleteOnTermination</code> attribute for volumes that are currently attached. The volume must be owned by the caller. If no value is specified for <code>DeleteOnTermination</code>, the default is <code>true</code> and the volume is deleted when the instance is terminated. You can't modify the <code>DeleteOnTermination</code> attribute for volumes that are attached to Amazon Web Services-managed resources.</p> <p>To add instance store volumes to an Amazon EBS-backed instance, you must add them when you launch the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html#Using_OverridingAMIBDM\">Update the block device mapping when launching an instance</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    disable_api_termination: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Enable or disable termination protection for the instance. If the value is <code>true</code>, you can't terminate the instance using the Amazon EC2 console, command line interface, or API. You can't enable termination protection for Spot Instances.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>Changes the instance type to the specified value. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html\">Instance types</a> in the <i>Amazon EC2 User Guide</i>. If the instance type is not valid, the error returned is <code>InvalidInstanceAttributeValue</code>.</p>"""
    kernel: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>Changes the instance's kernel to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html\">PV-GRUB</a>.</p>"""
    ramdisk: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>Changes the instance's RAM disk to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html\">PV-GRUB</a>.</p>"""
    user_data: NotRequired["aws_sdk_ec2.types.blob_attribute_value.BlobAttributeValue"]
    """<p>Changes the instance's user data to the specified value. User data must be base64-encoded. Depending on the tool or SDK that you're using, the base64-encoding might be performed for you. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-add-user-data.html\">Work with instance user data</a>.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "aws_sdk_ec2.types.attribute_value.AttributeValue"
    ]
    """<p>Specifies whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_id_string_list.GroupIdStringList"]
    """<p>Replaces the security groups of the instance with the specified security groups. You must specify the ID of at least one security group, even if it's just the default security group for the VPC.</p>"""
    ebs_optimized: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Specifies whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.</p>"""
    sriov_net_support: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>Set to <code>simple</code> to enable enhanced networking with the Intel 82599 Virtual Function interface for the instance.</p> <p>There is no way to disable enhanced networking with the Intel 82599 Virtual Function interface at this time.</p> <p>This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.</p>"""
    ena_support: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Set to <code>true</code> to enable enhanced networking with ENA for the instance.</p> <p>This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.</p>"""
