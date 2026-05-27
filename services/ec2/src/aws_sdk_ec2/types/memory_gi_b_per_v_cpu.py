"""Generated from Smithy shape ``com.amazonaws.ec2#MemoryGiBPerVCpu``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double


class MemoryGiBPerVCpu(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The minimum amount of memory per vCPU, in GiB. If this parameter is not specified, there is no minimum limit.</p>"""
    max: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The maximum amount of memory per vCPU, in GiB. If this parameter is not specified, there is no maximum limit.</p>"""
