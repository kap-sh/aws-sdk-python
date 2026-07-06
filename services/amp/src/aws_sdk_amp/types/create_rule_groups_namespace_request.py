"""Generated from Smithy shape ``com.amazonaws.amp#CreateRuleGroupsNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.rule_groups_namespace_data
    import aws_sdk_amp.types.rule_groups_namespace_name
    import aws_sdk_amp.types.tag_map
    import aws_sdk_amp.types.workspace_id


class CreateRuleGroupsNamespaceRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to add the rule groups namespace.</p>"""
    name: "aws_sdk_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
    """<p>The name for the new rule groups namespace.</p>"""
    data: "aws_sdk_amp.types.rule_groups_namespace_data.RuleGroupsNamespaceData"
    r"""<p>The rules file to use in the new namespace.</p> <p>Contains the base64-encoded version of the YAML rules file.</p> <p>For details about the rule groups namespace structure, see <a href=\"https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html\">RuleGroupsNamespaceData</a>.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""
    tags: NotRequired["aws_sdk_amp.types.tag_map.TagMap"]
    """<p>The list of tag keys and values to associate with the rule groups namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleGroupsNamespaceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_amp.types.rule_groups_namespace_data

    out["data"] = aws_sdk_amp.types.rule_groups_namespace_data.serialize_json(
        value["data"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRuleGroupsNamespaceRequest:
    out: CreateRuleGroupsNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRuleGroupsNamespaceRequest.name required")
    if "data" in data:
        import aws_sdk_amp.types.rule_groups_namespace_data

        out["data"] = aws_sdk_amp.types.rule_groups_namespace_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("CreateRuleGroupsNamespaceRequest.data required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.deserialize_json(data["tags"])
    return out
