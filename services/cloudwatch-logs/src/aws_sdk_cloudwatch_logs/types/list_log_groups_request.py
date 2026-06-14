"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListLogGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.account_ids
    import aws_sdk_cloudwatch_logs.types.data_source_filters
    import aws_sdk_cloudwatch_logs.types.field_index_names
    import aws_sdk_cloudwatch_logs.types.include_linked_accounts
    import aws_sdk_cloudwatch_logs.types.list_limit
    import aws_sdk_cloudwatch_logs.types.log_group_class
    import aws_sdk_cloudwatch_logs.types.log_group_name_regex_pattern
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.tag_filters


class ListLogGroupsRequest(TypedDict):
    log_group_name_pattern: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_name_regex_pattern.LogGroupNameRegexPattern"
    ]
    """<p>Use this parameter to limit the returned log groups to only those with names that match the pattern that you specify. This parameter is a regular expression that can match prefixes and substrings, and supports wildcard matching and matching multiple patterns, as in the following examples. </p> <ul> <li> <p>Use <code>^</code> to match log group names by prefix.</p> </li> <li> <p>For a substring match, specify the string to match. All matches are case sensitive</p> </li> <li> <p>To match multiple patterns, separate them with a <code>|</code> as in the example <code>^/aws/lambda|discovery</code> </p> </li> </ul> <p>You can specify as many as five different regular expression patterns in this field, each of which must be between 3 and 24 characters. You can include the <code>^</code> symbol as many as five times, and include the <code>|</code> symbol as many as four times.</p>"""
    log_group_class: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_class.LogGroupClass"
    ]
    """<p>Use this parameter to limit the results to only those log groups in the specified log group class. If you omit this parameter, log groups of all classes can be returned.</p>"""
    include_linked_accounts: NotRequired[
        "aws_sdk_cloudwatch_logs.types.include_linked_accounts.IncludeLinkedAccounts"
    ]
    """<p>If you are using a monitoring account, set this to <code>true</code> to have the operation return log groups in the accounts listed in <code>accountIdentifiers</code>.</p> <p>If this parameter is set to <code>true</code> and <code>accountIdentifiers</code> contains a null value, the operation returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account. </p> <p>The default for this parameter is <code>false</code>.</p>"""
    account_identifiers: NotRequired[
        "aws_sdk_cloudwatch_logs.types.account_ids.AccountIds"
    ]
    """<p>When <code>includeLinkedAccounts</code> is set to <code>true</code>, use this parameter to specify the list of accounts to search. You can specify as many as 20 account IDs in the array.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    limit: NotRequired["aws_sdk_cloudwatch_logs.types.list_limit.ListLimit"]
    """<p>The maximum number of log groups to return. If you omit this parameter, the default is up to 50 log groups.</p>"""
    data_sources: NotRequired[
        "aws_sdk_cloudwatch_logs.types.data_source_filters.DataSourceFilters"
    ]
    """<p>An array of data source filters to filter log groups by their associated data sources. You can filter by data source name, type, or both. Multiple filters within the same dimension are combined with OR logic, while filters across different dimensions are combined with AND logic.</p>"""
    field_index_names: NotRequired[
        "aws_sdk_cloudwatch_logs.types.field_index_names.FieldIndexNames"
    ]
    """<p>An array of field index names to filter log groups that have specific field indexes. Only log groups containing all specified field indexes are returned. You can specify 1 to 20 field index names, each with 1 to 512 characters.</p>"""
    log_group_tags: NotRequired["aws_sdk_cloudwatch_logs.types.tag_filters.TagFilters"]
    """<p>An array of tag filters to return only log groups that have specific tags. Multiple filters are combined with AND logic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogGroupsRequest) -> dict:
    out: dict = {}
    if "log_group_name_pattern" in value:
        out["logGroupNamePattern"] = value["log_group_name_pattern"]
    if "log_group_class" in value:
        import aws_sdk_cloudwatch_logs.types.log_group_class

        out["logGroupClass"] = (
            aws_sdk_cloudwatch_logs.types.log_group_class.serialize_aws_json_1_1(
                value["log_group_class"]
            )
        )
    if "include_linked_accounts" in value:
        out["includeLinkedAccounts"] = value["include_linked_accounts"]
    if "account_identifiers" in value:
        import aws_sdk_cloudwatch_logs.types.account_ids

        out["accountIdentifiers"] = (
            aws_sdk_cloudwatch_logs.types.account_ids.serialize_aws_json_1_1(
                value["account_identifiers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "data_sources" in value:
        import aws_sdk_cloudwatch_logs.types.data_source_filters

        out["dataSources"] = (
            aws_sdk_cloudwatch_logs.types.data_source_filters.serialize_aws_json_1_1(
                value["data_sources"]
            )
        )
    if "field_index_names" in value:
        import aws_sdk_cloudwatch_logs.types.field_index_names

        out["fieldIndexNames"] = (
            aws_sdk_cloudwatch_logs.types.field_index_names.serialize_aws_json_1_1(
                value["field_index_names"]
            )
        )
    if "log_group_tags" in value:
        import aws_sdk_cloudwatch_logs.types.tag_filters

        out["logGroupTags"] = (
            aws_sdk_cloudwatch_logs.types.tag_filters.serialize_aws_json_1_1(
                value["log_group_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogGroupsRequest:
    out: ListLogGroupsRequest = {}  # type: ignore[typeddict-item]
    if "logGroupNamePattern" in data:
        out["log_group_name_pattern"] = data["logGroupNamePattern"]
    if "logGroupClass" in data:
        import aws_sdk_cloudwatch_logs.types.log_group_class

        out["log_group_class"] = (
            aws_sdk_cloudwatch_logs.types.log_group_class.deserialize_aws_json_1_1(
                data["logGroupClass"]
            )
        )
    if "includeLinkedAccounts" in data:
        out["include_linked_accounts"] = data["includeLinkedAccounts"]
    if "accountIdentifiers" in data:
        import aws_sdk_cloudwatch_logs.types.account_ids

        out["account_identifiers"] = (
            aws_sdk_cloudwatch_logs.types.account_ids.deserialize_aws_json_1_1(
                data["accountIdentifiers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    if "dataSources" in data:
        import aws_sdk_cloudwatch_logs.types.data_source_filters

        out["data_sources"] = (
            aws_sdk_cloudwatch_logs.types.data_source_filters.deserialize_aws_json_1_1(
                data["dataSources"]
            )
        )
    if "fieldIndexNames" in data:
        import aws_sdk_cloudwatch_logs.types.field_index_names

        out["field_index_names"] = (
            aws_sdk_cloudwatch_logs.types.field_index_names.deserialize_aws_json_1_1(
                data["fieldIndexNames"]
            )
        )
    if "logGroupTags" in data:
        import aws_sdk_cloudwatch_logs.types.tag_filters

        out["log_group_tags"] = (
            aws_sdk_cloudwatch_logs.types.tag_filters.deserialize_aws_json_1_1(
                data["logGroupTags"]
            )
        )
    return out
