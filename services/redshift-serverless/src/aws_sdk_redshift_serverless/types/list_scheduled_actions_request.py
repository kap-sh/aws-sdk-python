"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListScheduledActionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.namespace_name
    import aws_sdk_redshift_serverless.types.pagination_token


class ListScheduledActionsRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. Use <code>nextToken</code> to display the next page of results.</p>"""
    namespace_name: NotRequired[
        "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName"
    ]
    """<p>The name of namespace associated with the scheduled action to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListScheduledActionsRequest) -> dict:
    out: dict = {}
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListScheduledActionsRequest:
    out: ListScheduledActionsRequest = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    return out
