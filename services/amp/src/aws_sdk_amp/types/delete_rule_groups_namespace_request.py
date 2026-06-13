"""Generated from Smithy shape ``com.amazonaws.amp#DeleteRuleGroupsNamespaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.rule_groups_namespace_name
    import aws_sdk_amp.types.workspace_id


class DeleteRuleGroupsNamespaceRequest(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace containing the rule groups namespace and definition to delete.</p>"""
    name: "aws_sdk_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
    """<p>The name of the rule groups namespace to delete.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRuleGroupsNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRuleGroupsNamespaceRequest:
    out: DeleteRuleGroupsNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
