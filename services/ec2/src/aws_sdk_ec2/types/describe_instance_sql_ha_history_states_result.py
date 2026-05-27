"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceSqlHaHistoryStatesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.registered_instance_list


class DescribeInstanceSqlHaHistoryStatesResult(TypedDict):
    instances: NotRequired[
        "aws_sdk_ec2.types.registered_instance_list.RegisteredInstanceList"
    ]
    """<p>Information about the historical SQL Server High Availability states of the SQL Server High Availability instances.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
