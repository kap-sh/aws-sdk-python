"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListAggregateLogGroupSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.account_ids
    import aws_sdk_cloudwatch_logs.types.data_source_filters
    import aws_sdk_cloudwatch_logs.types.include_linked_accounts
    import aws_sdk_cloudwatch_logs.types.list_aggregate_log_group_summaries_group_by
    import aws_sdk_cloudwatch_logs.types.list_log_groups_request_limit
    import aws_sdk_cloudwatch_logs.types.log_group_class
    import aws_sdk_cloudwatch_logs.types.log_group_name_regex_pattern
    import aws_sdk_cloudwatch_logs.types.next_token


class ListAggregateLogGroupSummariesRequest(TypedDict, closed=True):
    account_identifiers: NotRequired[
        "aws_sdk_cloudwatch_logs.types.account_ids.AccountIds"
    ]
    """<p>When <code>includeLinkedAccounts</code> is set to <code>true</code>, use this parameter to specify the list of accounts to search. You can specify as many as 20 account IDs in the array.</p>"""
    include_linked_accounts: NotRequired[
        "aws_sdk_cloudwatch_logs.types.include_linked_accounts.IncludeLinkedAccounts"
    ]
    """<p>If you are using a monitoring account, set this to <code>true</code> to have the operation return log groups in the accounts listed in <code>accountIdentifiers</code>.</p> <p>If this parameter is set to <code>true</code> and <code>accountIdentifiers</code> contains a null value, the operation returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account. </p> <p>The default for this parameter is <code>false</code>.</p>"""
    log_group_class: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_class.LogGroupClass"
    ]
    """<p>Filters the results by log group class to include only log groups of the specified class.</p>"""
    log_group_name_pattern: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_name_regex_pattern.LogGroupNameRegexPattern"
    ]
    """<p>Use this parameter to limit the returned log groups to only those with names that match the pattern that you specify. This parameter is a regular expression that can match prefixes and substrings, and supports wildcard matching and matching multiple patterns, as in the following examples. </p> <ul> <li> <p>Use <code>^</code> to match log group names by prefix.</p> </li> <li> <p>For a substring match, specify the string to match. All matches are case sensitive</p> </li> <li> <p>To match multiple patterns, separate them with a <code>|</code> as in the example <code>^/aws/lambda|discovery</code> </p> </li> </ul> <p>You can specify as many as five different regular expression patterns in this field, each of which must be between 3 and 24 characters. You can include the <code>^</code> symbol as many as five times, and include the <code>|</code> symbol as many as four times.</p>"""
    data_sources: NotRequired[
        "aws_sdk_cloudwatch_logs.types.data_source_filters.DataSourceFilters"
    ]
    """<p>Filters the results by data source characteristics to include only log groups associated with the specified data sources.</p>"""
    group_by: "aws_sdk_cloudwatch_logs.types.list_aggregate_log_group_summaries_group_by.ListAggregateLogGroupSummariesGroupBy"
    """<p>Specifies how to group the log groups in the summary.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    limit: NotRequired[
        "aws_sdk_cloudwatch_logs.types.list_log_groups_request_limit.ListLogGroupsRequestLimit"
    ]
    """<p>The maximum number of aggregated summaries to return. If you omit this parameter, the default is up to 50 aggregated summaries.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAggregateLogGroupSummariesRequest) -> dict:
    out: dict = {}
    if "account_identifiers" in value:
        import aws_sdk_cloudwatch_logs.types.account_ids

        out["accountIdentifiers"] = (
            aws_sdk_cloudwatch_logs.types.account_ids.serialize_aws_json_1_1(
                value["account_identifiers"]
            )
        )
    if "include_linked_accounts" in value:
        out["includeLinkedAccounts"] = value["include_linked_accounts"]
    if "log_group_class" in value:
        import aws_sdk_cloudwatch_logs.types.log_group_class

        out["logGroupClass"] = (
            aws_sdk_cloudwatch_logs.types.log_group_class.serialize_aws_json_1_1(
                value["log_group_class"]
            )
        )
    if "log_group_name_pattern" in value:
        out["logGroupNamePattern"] = value["log_group_name_pattern"]
    if "data_sources" in value:
        import aws_sdk_cloudwatch_logs.types.data_source_filters

        out["dataSources"] = (
            aws_sdk_cloudwatch_logs.types.data_source_filters.serialize_aws_json_1_1(
                value["data_sources"]
            )
        )
    import aws_sdk_cloudwatch_logs.types.list_aggregate_log_group_summaries_group_by

    out["groupBy"] = (
        aws_sdk_cloudwatch_logs.types.list_aggregate_log_group_summaries_group_by.serialize_aws_json_1_1(
            value["group_by"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAggregateLogGroupSummariesRequest:
    out: ListAggregateLogGroupSummariesRequest = {}  # type: ignore[typeddict-item]
    if "accountIdentifiers" in data:
        import aws_sdk_cloudwatch_logs.types.account_ids

        out["account_identifiers"] = (
            aws_sdk_cloudwatch_logs.types.account_ids.deserialize_aws_json_1_1(
                data["accountIdentifiers"]
            )
        )
    if "includeLinkedAccounts" in data:
        out["include_linked_accounts"] = data["includeLinkedAccounts"]
    if "logGroupClass" in data:
        import aws_sdk_cloudwatch_logs.types.log_group_class

        out["log_group_class"] = (
            aws_sdk_cloudwatch_logs.types.log_group_class.deserialize_aws_json_1_1(
                data["logGroupClass"]
            )
        )
    if "logGroupNamePattern" in data:
        out["log_group_name_pattern"] = data["logGroupNamePattern"]
    if "dataSources" in data:
        import aws_sdk_cloudwatch_logs.types.data_source_filters

        out["data_sources"] = (
            aws_sdk_cloudwatch_logs.types.data_source_filters.deserialize_aws_json_1_1(
                data["dataSources"]
            )
        )
    if "groupBy" in data:
        import aws_sdk_cloudwatch_logs.types.list_aggregate_log_group_summaries_group_by

        out["group_by"] = (
            aws_sdk_cloudwatch_logs.types.list_aggregate_log_group_summaries_group_by.deserialize_aws_json_1_1(
                data["groupBy"]
            )
        )
    else:
        raise DeserializationError(
            "ListAggregateLogGroupSummariesRequest.group_by required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    return out
