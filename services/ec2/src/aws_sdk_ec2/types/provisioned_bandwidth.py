"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionedBandwidth``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string


class ProvisionedBandwidth(TypedDict):
    provision_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>Reserved.</p>"""
    provisioned: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    request_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>Reserved.</p>"""
    requested: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
