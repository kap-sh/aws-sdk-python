"""Generated from Smithy shape ``com.amazonaws.ec2#RegionalSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class RegionalSummary(TypedDict):
    region_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region.</p>"""
    number_of_matched_accounts: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of accounts in the Region with the same configuration value for the attribute that is most frequently observed.</p>"""
    number_of_unmatched_accounts: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of accounts in the Region with a configuration value different from the most frequently observed value for the attribute.</p>"""
