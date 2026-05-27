"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceAttachmentEnaSrdUdpSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class InstanceAttachmentEnaSrdUdpSpecification(TypedDict):
    ena_srd_udp_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether UDP traffic to and from the instance uses ENA Express. To specify this setting, you must first enable ENA Express.</p>"""
