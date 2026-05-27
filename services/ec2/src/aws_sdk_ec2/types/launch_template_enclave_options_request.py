"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateEnclaveOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class LaunchTemplateEnclaveOptionsRequest(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>To enable the instance for Amazon Web Services Nitro Enclaves, set this parameter to <code>true</code>.</p>"""
