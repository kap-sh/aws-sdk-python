"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAggregateIdFormatResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.id_format_list


class DescribeAggregateIdFormatResult(TypedDict):
    use_long_ids_aggregated: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether all resource types in the Region are configured to use longer IDs. This value is only <code>true</code> if all users are configured to use longer IDs for all resources types in the Region.</p>"""
    statuses: NotRequired["aws_sdk_ec2.types.id_format_list.IdFormatList"]
    """<p>Information about each resource's ID format.</p>"""
