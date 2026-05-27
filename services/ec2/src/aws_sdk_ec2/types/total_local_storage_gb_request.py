"""Generated from Smithy shape ``com.amazonaws.ec2#TotalLocalStorageGBRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double


class TotalLocalStorageGBRequest(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The minimum amount of total local storage, in GB. To specify no minimum limit, omit this parameter.</p>"""
    max: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The maximum amount of total local storage, in GB. To specify no maximum limit, omit this parameter.</p>"""
