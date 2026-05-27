"""Generated from Smithy shape ``com.amazonaws.ec2#AddressAttribute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id
    import aws_sdk_ec2.types.ptr_update_status
    import aws_sdk_ec2.types.public_ip_address
    import aws_sdk_ec2.types.string


class AddressAttribute(TypedDict):
    public_ip: NotRequired["aws_sdk_ec2.types.public_ip_address.PublicIpAddress"]
    """<p>The public IP address.</p>"""
    allocation_id: NotRequired["aws_sdk_ec2.types.allocation_id.AllocationId"]
    """<p>[EC2-VPC] The allocation ID.</p>"""
    ptr_record: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The pointer (PTR) record for the IP address.</p>"""
    ptr_record_update: NotRequired[
        "aws_sdk_ec2.types.ptr_update_status.PtrUpdateStatus"
    ]
    """<p>The updated PTR record for the IP address.</p>"""
