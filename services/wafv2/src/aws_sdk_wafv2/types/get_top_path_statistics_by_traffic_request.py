"""Generated from Smithy shape ``com.amazonaws.wafv2#GetTopPathStatisticsByTrafficRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.filter_string
    import aws_sdk_wafv2.types.next_marker
    import aws_sdk_wafv2.types.number_of_top_traffic_bots_per_path
    import aws_sdk_wafv2.types.path_statistics_limit
    import aws_sdk_wafv2.types.resource_arn
    import aws_sdk_wafv2.types.scope
    import aws_sdk_wafv2.types.time_window
    import aws_sdk_wafv2.types.uri_path_prefix_string


class GetTopPathStatisticsByTrafficRequest(TypedDict):
    web_acl_arn: "aws_sdk_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL for which you want to retrieve path statistics.</p>"""
    scope: "aws_sdk_wafv2.types.scope.Scope"
    """<p>Specifies whether the web ACL is for an Amazon Web Services CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer, an AppSync GraphQL API, an Amazon Cognito user pool, an Amazon Web Services App Runner service, or an Amazon Web Services Verified Access instance.</p>"""
    uri_path_prefix: NotRequired[
        "aws_sdk_wafv2.types.uri_path_prefix_string.UriPathPrefixString"
    ]
    """<p>A URI path prefix to filter the results. When you specify this parameter, the operation returns statistics for individual URIs within the specified path prefix. For example, if you specify <code>/api</code>, the response includes statistics for paths like <code>/api/v1/users</code> and <code>/api/v2/orders</code>. If you don't specify this parameter, the operation returns top-level path statistics.</p>"""
    time_window: "aws_sdk_wafv2.types.time_window.TimeWindow"
    """<p>The time window for which you want to retrieve path statistics. The time window must be within the data retention period for your web ACL.</p>"""
    bot_category: NotRequired["aws_sdk_wafv2.types.filter_string.FilterString"]
    """<p>Filters the results to include only traffic from bots in the specified category. For example, you can filter by <code>ai</code> to see only AI crawler traffic, or <code>search_engine</code> to see only search engine bot traffic. When you apply this filter, the <code>Source</code> field is populated in the response.</p>"""
    bot_organization: NotRequired["aws_sdk_wafv2.types.filter_string.FilterString"]
    """<p>Filters the results to include only traffic from bots belonging to the specified organization. For example, you can filter by <code>openai</code> or <code>google</code>. When you apply this filter, the <code>Source</code> field is populated in the response.</p>"""
    bot_name: NotRequired["aws_sdk_wafv2.types.filter_string.FilterString"]
    """<p>Filters the results to include only traffic from the specified bot. For example, you can filter by <code>gptbot</code> or <code>googlebot</code>. When you apply this filter, the <code>Source</code> field is populated in the response.</p>"""
    limit: "aws_sdk_wafv2.types.path_statistics_limit.PathStatisticsLimit"
    """<p>The maximum number of path statistics to return. Valid values are 1 to 100.</p>"""
    number_of_top_traffic_bots_per_path: "aws_sdk_wafv2.types.number_of_top_traffic_bots_per_path.NumberOfTopTrafficBotsPerPath"
    """<p>The maximum number of top bots to include in the statistics for each path. Valid values are 1 to 10.</p>"""
    next_marker: NotRequired["aws_sdk_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTopPathStatisticsByTrafficRequest) -> dict:
    out: dict = {}
    out["WebAclArn"] = value["web_acl_arn"]
    import aws_sdk_wafv2.types.scope

    out["Scope"] = aws_sdk_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    if "uri_path_prefix" in value:
        out["UriPathPrefix"] = value["uri_path_prefix"]
    import aws_sdk_wafv2.types.time_window

    out["TimeWindow"] = aws_sdk_wafv2.types.time_window.serialize_aws_json_1_1(
        value["time_window"]
    )
    if "bot_category" in value:
        out["BotCategory"] = value["bot_category"]
    if "bot_organization" in value:
        out["BotOrganization"] = value["bot_organization"]
    if "bot_name" in value:
        out["BotName"] = value["bot_name"]
    out["Limit"] = value["limit"]
    out["NumberOfTopTrafficBotsPerPath"] = value["number_of_top_traffic_bots_per_path"]
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTopPathStatisticsByTrafficRequest:
    out: GetTopPathStatisticsByTrafficRequest = {}  # type: ignore[typeddict-item]
    if "WebAclArn" in data:
        out["web_acl_arn"] = data["WebAclArn"]
    else:
        raise DeserializationError(
            "GetTopPathStatisticsByTrafficRequest.web_acl_arn required"
        )
    if "Scope" in data:
        import aws_sdk_wafv2.types.scope

        out["scope"] = aws_sdk_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError(
            "GetTopPathStatisticsByTrafficRequest.scope required"
        )
    if "UriPathPrefix" in data:
        out["uri_path_prefix"] = data["UriPathPrefix"]
    if "TimeWindow" in data:
        import aws_sdk_wafv2.types.time_window

        out["time_window"] = aws_sdk_wafv2.types.time_window.deserialize_aws_json_1_1(
            data["TimeWindow"]
        )
    else:
        raise DeserializationError(
            "GetTopPathStatisticsByTrafficRequest.time_window required"
        )
    if "BotCategory" in data:
        out["bot_category"] = data["BotCategory"]
    if "BotOrganization" in data:
        out["bot_organization"] = data["BotOrganization"]
    if "BotName" in data:
        out["bot_name"] = data["BotName"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        raise DeserializationError(
            "GetTopPathStatisticsByTrafficRequest.limit required"
        )
    if "NumberOfTopTrafficBotsPerPath" in data:
        out["number_of_top_traffic_bots_per_path"] = data[
            "NumberOfTopTrafficBotsPerPath"
        ]
    else:
        raise DeserializationError(
            "GetTopPathStatisticsByTrafficRequest.number_of_top_traffic_bots_per_path required"
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
