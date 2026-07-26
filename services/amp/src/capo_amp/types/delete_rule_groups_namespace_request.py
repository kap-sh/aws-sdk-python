"""Generated from Smithy shape ``com.amazonaws.amp#DeleteRuleGroupsNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.idempotency_token
    import capo_amp.types.rule_groups_namespace_name
    import capo_amp.types.workspace_id


class DeleteRuleGroupsNamespaceRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace containing the rule groups namespace and definition to delete.</p>"""
    name: "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
    """<p>The name of the rule groups namespace to delete.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRuleGroupsNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRuleGroupsNamespaceRequest:
    out: DeleteRuleGroupsNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
