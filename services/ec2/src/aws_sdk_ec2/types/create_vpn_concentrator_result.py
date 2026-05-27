"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnConcentratorResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_concentrator


class CreateVpnConcentratorResult(TypedDict):
    vpn_concentrator: NotRequired["aws_sdk_ec2.types.vpn_concentrator.VpnConcentrator"]
    """<p>Information about the VPN concentrator.</p>"""
