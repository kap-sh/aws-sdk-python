"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceUefiDataResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.string


class GetInstanceUefiDataResult(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance from which to retrieve the UEFI data.</p>"""
    uefi_data: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Base64 representation of the non-volatile UEFI variable store.</p>"""
