"""Generated from Smithy shape ``com.amazonaws.ec2#BlockDeviceMappingResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ebs_block_device_response
    import aws_sdk_ec2.types.string


class BlockDeviceMappingResponse(TypedDict):
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</p>"""
    virtual_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The virtual device name.</p>"""
    ebs: NotRequired[
        "aws_sdk_ec2.types.ebs_block_device_response.EbsBlockDeviceResponse"
    ]
    """<p>Parameters used to automatically set up EBS volumes when the instance is launched.</p>"""
    no_device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Suppresses the specified device included in the block device mapping.</p>"""
