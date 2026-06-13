"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListUsageLimitsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.usage_limits


class ListUsageLimitsResponse(TypedDict):
    usage_limits: NotRequired[
        "aws_sdk_redshift_serverless.types.usage_limits.UsageLimits"
    ]
    """<p>An array of returned usage limit objects.</p>"""
    next_token: NotRequired[
        "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsageLimitsResponse) -> dict:
    out: dict = {}
    if "usage_limits" in value:
        import aws_sdk_redshift_serverless.types.usage_limits

        out["usageLimits"] = (
            aws_sdk_redshift_serverless.types.usage_limits.serialize_aws_json_1_1(
                value["usage_limits"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsageLimitsResponse:
    out: ListUsageLimitsResponse = {}  # type: ignore[typeddict-item]
    if "usageLimits" in data:
        import aws_sdk_redshift_serverless.types.usage_limits

        out["usage_limits"] = (
            aws_sdk_redshift_serverless.types.usage_limits.deserialize_aws_json_1_1(
                data["usageLimits"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
