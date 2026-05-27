"""Generated from Smithy shape ``com.amazonaws.ec2#AttributeSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.regional_summary_list
    import aws_sdk_ec2.types.string


class AttributeSummary(TypedDict):
    attribute_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the attribute.</p>"""
    most_frequent_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The configuration value that is most frequently observed for the attribute.</p>"""
    number_of_matched_accounts: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of accounts with the same configuration value for the attribute that is most frequently observed.</p>"""
    number_of_unmatched_accounts: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of accounts with a configuration value different from the most frequently observed value for the attribute.</p>"""
    regional_summaries: NotRequired[
        "aws_sdk_ec2.types.regional_summary_list.RegionalSummaryList"
    ]
    """<p>The summary report for each Region for the attribute.</p>"""
