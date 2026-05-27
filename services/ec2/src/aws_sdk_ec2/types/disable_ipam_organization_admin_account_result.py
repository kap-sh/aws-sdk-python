"""Generated from Smithy shape ``com.amazonaws.ec2#DisableIpamOrganizationAdminAccountResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class DisableIpamOrganizationAdminAccountResult(TypedDict):
    success: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The result of disabling the IPAM account.</p>"""
