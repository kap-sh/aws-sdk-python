"""Generated from Smithy shape ``com.amazonaws.ec2#EnaSrdSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ena_srd_udp_specification


class EnaSrdSpecification(TypedDict):
    ena_srd_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether ENA Express is enabled for the network interface.</p>"""
    ena_srd_udp_specification: NotRequired[
        "aws_sdk_ec2.types.ena_srd_udp_specification.EnaSrdUdpSpecification"
    ]
    """<p>Configures ENA Express for UDP network traffic.</p>"""
