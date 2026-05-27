"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceAttribute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_boolean_value
    import aws_sdk_ec2.types.attribute_value
    import aws_sdk_ec2.types.enclave_options
    import aws_sdk_ec2.types.group_identifier_list
    import aws_sdk_ec2.types.instance_block_device_mapping_list
    import aws_sdk_ec2.types.product_code_list
    import aws_sdk_ec2.types.string


class InstanceAttribute(TypedDict):
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.instance_block_device_mapping_list.InstanceBlockDeviceMappingList"
    ]
    """<p>The block device mapping of the instance.</p>"""
    disable_api_termination: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether termination protection is enabled. If the value is <code>true</code>, you can't terminate the instance using the Amazon EC2 console, command line tools, or API.</p>"""
    ena_support: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether enhanced networking with ENA is enabled.</p>"""
    enclave_options: NotRequired["aws_sdk_ec2.types.enclave_options.EnclaveOptions"]
    """<p>Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.</p>"""
    ebs_optimized: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether the instance is optimized for Amazon EBS I/O.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "aws_sdk_ec2.types.attribute_value.AttributeValue"
    ]
    """<p>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The instance type.</p>"""
    kernel_id: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The kernel ID.</p>"""
    product_codes: NotRequired["aws_sdk_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes.</p>"""
    ramdisk_id: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The RAM disk ID.</p>"""
    root_device_name: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The device name of the root device volume (for example, <code>/dev/sda1</code>).</p>"""
    source_dest_check: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether source/destination checks are enabled.</p>"""
    sriov_net_support: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.</p>"""
    user_data: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The user data.</p>"""
    disable_api_stop: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether stop protection is enabled for the instance.</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>The security groups associated with the instance.</p>"""
