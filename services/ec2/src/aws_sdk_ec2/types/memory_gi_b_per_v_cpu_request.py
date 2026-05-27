"""Generated from Smithy shape ``com.amazonaws.ec2#MemoryGiBPerVCpuRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double


class MemoryGiBPerVCpuRequest(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The minimum amount of memory per vCPU, in GiB. To specify no minimum limit, omit this parameter.</p>"""
    max: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The maximum amount of memory per vCPU, in GiB. To specify no maximum limit, omit this parameter.</p>"""
