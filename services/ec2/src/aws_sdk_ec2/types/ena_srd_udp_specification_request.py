"""Generated from Smithy shape ``com.amazonaws.ec2#EnaSrdUdpSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class EnaSrdUdpSpecificationRequest(TypedDict):
    ena_srd_udp_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether UDP traffic uses ENA Express for your instance. To ensure that UDP traffic can use ENA Express when you launch an instance, you must also set <b>EnaSrdEnabled</b> in the <b>EnaSrdSpecificationRequest</b> to <code>true</code>.</p>"""
