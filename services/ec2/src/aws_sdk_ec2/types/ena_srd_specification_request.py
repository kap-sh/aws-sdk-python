"""Generated from Smithy shape ``com.amazonaws.ec2#EnaSrdSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ena_srd_udp_specification_request


class EnaSrdSpecificationRequest(TypedDict):
    ena_srd_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether ENA Express is enabled for the network interface when you launch an instance.</p>"""
    ena_srd_udp_specification: NotRequired[
        "aws_sdk_ec2.types.ena_srd_udp_specification_request.EnaSrdUdpSpecificationRequest"
    ]
    """<p>Contains ENA Express settings for UDP network traffic for the network interface attached to the instance.</p>"""
