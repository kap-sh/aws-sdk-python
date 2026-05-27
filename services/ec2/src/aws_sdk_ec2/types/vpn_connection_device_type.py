"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnectionDeviceType``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class VpnConnectionDeviceType(TypedDict):
    vpn_connection_device_type_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Customer gateway device identifier.</p>"""
    vendor: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Customer gateway device vendor.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Customer gateway device platform.</p>"""
    software: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Customer gateway device software version.</p>"""
