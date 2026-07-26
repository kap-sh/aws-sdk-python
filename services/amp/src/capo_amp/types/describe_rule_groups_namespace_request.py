"""Generated from Smithy shape ``com.amazonaws.amp#DescribeRuleGroupsNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.rule_groups_namespace_name
    import capo_amp.types.workspace_id


class DescribeRuleGroupsNamespaceRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace containing the rule groups namespace.</p>"""
    name: "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
    """<p>The name of the rule groups namespace that you want information for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRuleGroupsNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRuleGroupsNamespaceRequest:
    out: DescribeRuleGroupsNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
