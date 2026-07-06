"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListUsageLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.usage_limit_usage_type


class ListUsageLimitsRequest(TypedDict, closed=True):
    resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) associated with the resource whose usage limits you want to list.</p>"""
    usage_type: NotRequired[
        "aws_sdk_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType"
    ]
    """<p>The Amazon Redshift Serverless feature whose limits you want to see.</p>"""
    next_token: NotRequired[
        "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>If your initial <code>ListUsageLimits</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListUsageLimits</code> operations, which returns results in the next page. </p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsageLimitsRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "usage_type" in value:
        out["usageType"] = value["usage_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsageLimitsRequest:
    out: ListUsageLimitsRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    return out
