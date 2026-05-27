"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeContributorInsightsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.contributor_insights_mode
    import aws_sdk_dynamodb.types.contributor_insights_rule_list
    import aws_sdk_dynamodb.types.contributor_insights_status
    import aws_sdk_dynamodb.types.failure_exception
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.last_update_date_time
    import aws_sdk_dynamodb.types.table_name


class DescribeContributorInsightsOutput(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>The name of the table being described.</p>"""
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index being described.</p>"""
    contributor_insights_rule_list: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_rule_list.ContributorInsightsRuleList"
    ]
    """<p>List of names of the associated contributor insights rules.</p>"""
    contributor_insights_status: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_status.ContributorInsightsStatus"
    ]
    """<p>Current status of contributor insights.</p>"""
    last_update_date_time: NotRequired[
        "aws_sdk_dynamodb.types.last_update_date_time.LastUpdateDateTime"
    ]
    """<p>Timestamp of the last time the status was changed.</p>"""
    failure_exception: NotRequired[
        "aws_sdk_dynamodb.types.failure_exception.FailureException"
    ]
    """<p>Returns information about the last failure that was encountered.</p> <p>The most common exceptions for a FAILED status are:</p> <ul> <li> <p>LimitExceededException - Per-account Amazon CloudWatch Contributor Insights rule limit reached. Please disable Contributor Insights for other tables/indexes OR disable Contributor Insights rules before retrying.</p> </li> <li> <p>AccessDeniedException - Amazon CloudWatch Contributor Insights rules cannot be modified due to insufficient permissions.</p> </li> <li> <p>AccessDeniedException - Failed to create service-linked role for Contributor Insights due to insufficient permissions.</p> </li> <li> <p>InternalServerError - Failed to create Amazon CloudWatch Contributor Insights rules. Please retry request.</p> </li> </ul>"""
    contributor_insights_mode: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_mode.ContributorInsightsMode"
    ]
    """<p>The mode of CloudWatch Contributor Insights for DynamoDB that determines which events are emitted. Can be set to track all access and throttled events or throttled events only.</p>"""
