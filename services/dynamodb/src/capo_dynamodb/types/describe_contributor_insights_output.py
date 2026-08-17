"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeContributorInsightsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.contributor_insights_mode
    import capo_dynamodb.types.contributor_insights_rule_list
    import capo_dynamodb.types.contributor_insights_status
    import capo_dynamodb.types.failure_exception
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.last_update_date_time
    import capo_dynamodb.types.table_name


class DescribeContributorInsightsOutput(TypedDict, closed=True):
    table_name: NotRequired["capo_dynamodb.types.table_name.TableName"]
    """<p>The name of the table being described.</p>"""
    index_name: NotRequired["capo_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index being described.</p>"""
    contributor_insights_rule_list: NotRequired[
        "capo_dynamodb.types.contributor_insights_rule_list.ContributorInsightsRuleList"
    ]
    """<p>List of names of the associated contributor insights rules.</p>"""
    contributor_insights_status: NotRequired[
        "capo_dynamodb.types.contributor_insights_status.ContributorInsightsStatus"
    ]
    """<p>Current status of contributor insights.</p>"""
    last_update_date_time: NotRequired[
        "capo_dynamodb.types.last_update_date_time.LastUpdateDateTime"
    ]
    """<p>Timestamp of the last time the status was changed.</p>"""
    failure_exception: NotRequired[
        "capo_dynamodb.types.failure_exception.FailureException"
    ]
    """<p>Returns information about the last failure that was encountered.</p> <p>The most common exceptions for a FAILED status are:</p> <ul> <li> <p>LimitExceededException - Per-account Amazon CloudWatch Contributor Insights rule limit reached. Please disable Contributor Insights for other tables/indexes OR disable Contributor Insights rules before retrying.</p> </li> <li> <p>AccessDeniedException - Amazon CloudWatch Contributor Insights rules cannot be modified due to insufficient permissions.</p> </li> <li> <p>AccessDeniedException - Failed to create service-linked role for Contributor Insights due to insufficient permissions.</p> </li> <li> <p>InternalServerError - Failed to create Amazon CloudWatch Contributor Insights rules. Please retry request.</p> </li> </ul>"""
    contributor_insights_mode: NotRequired[
        "capo_dynamodb.types.contributor_insights_mode.ContributorInsightsMode"
    ]
    """<p>The mode of CloudWatch Contributor Insights for DynamoDB that determines which events are emitted. Can be set to track all access and throttled events or throttled events only.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeContributorInsightsOutput) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "contributor_insights_rule_list" in value:
        import capo_dynamodb.types.contributor_insights_rule_list

        out["ContributorInsightsRuleList"] = (
            capo_dynamodb.types.contributor_insights_rule_list.serialize_aws_json_1_0(
                value["contributor_insights_rule_list"]
            )
        )
    if "contributor_insights_status" in value:
        import capo_dynamodb.types.contributor_insights_status

        out["ContributorInsightsStatus"] = (
            capo_dynamodb.types.contributor_insights_status.serialize_aws_json_1_0(
                value["contributor_insights_status"]
            )
        )
    if "last_update_date_time" in value:
        import capo_dynamodb.types.last_update_date_time

        out["LastUpdateDateTime"] = (
            capo_dynamodb.types.last_update_date_time.serialize_aws_json_1_0(
                value["last_update_date_time"]
            )
        )
    if "failure_exception" in value:
        import capo_dynamodb.types.failure_exception

        out["FailureException"] = (
            capo_dynamodb.types.failure_exception.serialize_aws_json_1_0(
                value["failure_exception"]
            )
        )
    if "contributor_insights_mode" in value:
        import capo_dynamodb.types.contributor_insights_mode

        out["ContributorInsightsMode"] = (
            capo_dynamodb.types.contributor_insights_mode.serialize_aws_json_1_0(
                value["contributor_insights_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeContributorInsightsOutput:
    out: DescribeContributorInsightsOutput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    if data.get("ContributorInsightsRuleList") is not None:
        import capo_dynamodb.types.contributor_insights_rule_list

        out["contributor_insights_rule_list"] = (
            capo_dynamodb.types.contributor_insights_rule_list.deserialize_aws_json_1_0(
                data["ContributorInsightsRuleList"]
            )
        )
    if data.get("ContributorInsightsStatus") is not None:
        import capo_dynamodb.types.contributor_insights_status

        out["contributor_insights_status"] = (
            capo_dynamodb.types.contributor_insights_status.deserialize_aws_json_1_0(
                data["ContributorInsightsStatus"]
            )
        )
    if data.get("LastUpdateDateTime") is not None:
        import capo_dynamodb.types.last_update_date_time

        out["last_update_date_time"] = (
            capo_dynamodb.types.last_update_date_time.deserialize_aws_json_1_0(
                data["LastUpdateDateTime"]
            )
        )
    if data.get("FailureException") is not None:
        import capo_dynamodb.types.failure_exception

        out["failure_exception"] = (
            capo_dynamodb.types.failure_exception.deserialize_aws_json_1_0(
                data["FailureException"]
            )
        )
    if data.get("ContributorInsightsMode") is not None:
        import capo_dynamodb.types.contributor_insights_mode

        out["contributor_insights_mode"] = (
            capo_dynamodb.types.contributor_insights_mode.deserialize_aws_json_1_0(
                data["ContributorInsightsMode"]
            )
        )
    return out
