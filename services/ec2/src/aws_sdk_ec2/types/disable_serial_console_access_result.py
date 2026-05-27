"""Generated from Smithy shape ``com.amazonaws.ec2#DisableSerialConsoleAccessResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class DisableSerialConsoleAccessResult(TypedDict):
    serial_console_access_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, access to the EC2 serial console of all instances is enabled for your account. If <code>false</code>, access to the EC2 serial console of all instances is disabled for your account.</p>"""
