"""Generated from Smithy shape ``com.amazonaws.ec2#PciId``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PciId(TypedDict):
    device_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the device.</p>"""
    vendor_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the vendor.</p>"""
    subsystem_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subsystem.</p>"""
    subsystem_vendor_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the vendor for the subsystem.</p>"""
