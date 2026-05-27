"""Generated from Smithy shape ``com.amazonaws.ec2#GetSerialConsoleAccessStatusResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.managed_by


class GetSerialConsoleAccessStatusResult(TypedDict):
    serial_console_access_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, access to the EC2 serial console of all instances is enabled for your account. If <code>false</code>, access to the EC2 serial console of all instances is disabled for your account.</p>"""
    managed_by: NotRequired["aws_sdk_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages access to the serial console. Possible values include:</p> <ul> <li> <p> <code>account</code> - Access is managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - Access is managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""
