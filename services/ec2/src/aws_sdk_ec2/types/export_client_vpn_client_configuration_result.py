"""Generated from Smithy shape ``com.amazonaws.ec2#ExportClientVpnClientConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ExportClientVpnClientConfigurationResult(TypedDict):
    client_configuration: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The contents of the Client VPN endpoint configuration file.</p>"""
