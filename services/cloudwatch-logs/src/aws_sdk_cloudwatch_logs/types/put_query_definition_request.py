"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutQueryDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.client_token
    import aws_sdk_cloudwatch_logs.types.log_group_names
    import aws_sdk_cloudwatch_logs.types.query_definition_name
    import aws_sdk_cloudwatch_logs.types.query_definition_string
    import aws_sdk_cloudwatch_logs.types.query_id
    import aws_sdk_cloudwatch_logs.types.query_language
    import aws_sdk_cloudwatch_logs.types.query_parameter_list


class PutQueryDefinitionRequest(TypedDict):
    query_language: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_language.QueryLanguage"
    ]
    r"""<p>Specify the query language to use for this query. The options are Logs Insights QL, OpenSearch PPL, and OpenSearch SQL. For more information about the query languages that CloudWatch Logs supports, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html\">Supported query languages</a>.</p>"""
    name: "aws_sdk_cloudwatch_logs.types.query_definition_name.QueryDefinitionName"
    r"""<p>A name for the query definition. If you are saving numerous query definitions, we recommend that you name them. This way, you can find the ones you want by using the first part of the name as a filter in the <code>queryDefinitionNamePrefix</code> parameter of <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.html\">DescribeQueryDefinitions</a>.</p>"""
    query_definition_id: NotRequired["aws_sdk_cloudwatch_logs.types.query_id.QueryId"]
    r"""<p>If you are updating a query definition, use this parameter to specify the ID of the query definition that you want to update. You can use <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.html\">DescribeQueryDefinitions</a> to retrieve the IDs of your saved query definitions.</p> <p>If you are creating a query definition, do not specify this parameter. CloudWatch generates a unique ID for the new query definition and include it in the response to this operation.</p>"""
    log_group_names: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_names.LogGroupNames"
    ]
    """<p>Use this parameter to include specific log groups as part of your query definition. If your query uses the OpenSearch Service query language, you specify the log group names inside the <code>querystring</code> instead of here.</p> <p>If you are updating an existing query definition for the Logs Insights QL or OpenSearch Service PPL and you omit this parameter, then the updated definition will contain no log groups.</p>"""
    query_string: (
        "aws_sdk_cloudwatch_logs.types.query_definition_string.QueryDefinitionString"
    )
    r"""<p>The query string to use for this definition. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html\">CloudWatch Logs Insights Query Syntax</a>.</p>"""
    client_token: NotRequired["aws_sdk_cloudwatch_logs.types.client_token.ClientToken"]
    """<p>Used as an idempotency token, to avoid returning an exception if the service receives the same request twice because of a network error.</p>"""
    parameters: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_parameter_list.QueryParameterList"
    ]
    """<p>Use this parameter to include specific query parameters as part of your query definition. Query parameters are supported only for Logs Insights QL queries. Query parameters allow you to use placeholder variables in your query string that are substituted with values at execution time. Use the <code>{{parameterName}}</code> syntax in your query string to reference a parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutQueryDefinitionRequest) -> dict:
    out: dict = {}
    if "query_language" in value:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["queryLanguage"] = (
            aws_sdk_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
                value["query_language"]
            )
        )
    out["name"] = value["name"]
    if "query_definition_id" in value:
        out["queryDefinitionId"] = value["query_definition_id"]
    if "log_group_names" in value:
        import aws_sdk_cloudwatch_logs.types.log_group_names

        out["logGroupNames"] = (
            aws_sdk_cloudwatch_logs.types.log_group_names.serialize_aws_json_1_1(
                value["log_group_names"]
            )
        )
    out["queryString"] = value["query_string"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "parameters" in value:
        import aws_sdk_cloudwatch_logs.types.query_parameter_list

        out["parameters"] = (
            aws_sdk_cloudwatch_logs.types.query_parameter_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutQueryDefinitionRequest:
    out: PutQueryDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "queryLanguage" in data:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["query_language"] = (
            aws_sdk_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PutQueryDefinitionRequest.name required")
    if "queryDefinitionId" in data:
        out["query_definition_id"] = data["queryDefinitionId"]
    if "logGroupNames" in data:
        import aws_sdk_cloudwatch_logs.types.log_group_names

        out["log_group_names"] = (
            aws_sdk_cloudwatch_logs.types.log_group_names.deserialize_aws_json_1_1(
                data["logGroupNames"]
            )
        )
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError("PutQueryDefinitionRequest.query_string required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "parameters" in data:
        import aws_sdk_cloudwatch_logs.types.query_parameter_list

        out["parameters"] = (
            aws_sdk_cloudwatch_logs.types.query_parameter_list.deserialize_aws_json_1_1(
                data["parameters"]
            )
        )
    return out
