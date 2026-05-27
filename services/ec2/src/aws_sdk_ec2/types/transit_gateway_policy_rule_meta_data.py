"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyRuleMetaData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class TransitGatewayPolicyRuleMetaData(TypedDict):
    meta_data_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key name for the transit gateway policy rule meta data tag.</p>"""
    meta_data_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value of the key for the transit gateway policy rule meta data tag.</p>"""
