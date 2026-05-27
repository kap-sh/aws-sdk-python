"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnConnectionDeviceSampleConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_connection_device_sample_configuration


class GetVpnConnectionDeviceSampleConfigurationResult(TypedDict):
    vpn_connection_device_sample_configuration: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_device_sample_configuration.VpnConnectionDeviceSampleConfiguration"
    ]
    """<p>Sample configuration file for the specified customer gateway device.</p>"""
