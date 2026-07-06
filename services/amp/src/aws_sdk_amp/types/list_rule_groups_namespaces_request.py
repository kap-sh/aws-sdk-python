"""Generated from Smithy shape ``com.amazonaws.amp#ListRuleGroupsNamespacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.pagination_token
    import aws_sdk_amp.types.rule_groups_namespace_name
    import aws_sdk_amp.types.workspace_id


class ListRuleGroupsNamespacesRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace containing the rule groups namespaces.</p>"""
    name: NotRequired[
        "aws_sdk_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
    ]
    """<p>Use this parameter to filter the rule groups namespaces that are returned. Only the namespaces with names that begin with the value that you specify are returned.</p>"""
    next_token: NotRequired["aws_sdk_amp.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of items to return. You receive this token from a previous call, and use it to get the next page of results. The other parameters must be the same as the initial call.</p> <p>For example, if your initial request has <code>maxResults</code> of 10, and there are 12 rule groups namespaces to return, then your initial request will return 10 and a <code>nextToken</code>. Using the next token in a subsequent call will return the remaining 2 namespaces.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return. The default is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRuleGroupsNamespacesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRuleGroupsNamespacesRequest:
    out: ListRuleGroupsNamespacesRequest = {}  # type: ignore[typeddict-item]
    return out
