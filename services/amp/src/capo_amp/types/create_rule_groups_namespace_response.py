"""Generated from Smithy shape ``com.amazonaws.amp#CreateRuleGroupsNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.rule_groups_namespace_arn
    import capo_amp.types.rule_groups_namespace_name
    import capo_amp.types.rule_groups_namespace_status
    import capo_amp.types.tag_map


class CreateRuleGroupsNamespaceResponse(TypedDict, closed=True):
    name: "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
    """<p>The name of the new rule groups namespace.</p>"""
    arn: "capo_amp.types.rule_groups_namespace_arn.RuleGroupsNamespaceArn"
    """<p>The Amazon Resource Name (ARN) of the new rule groups namespace.</p>"""
    status: "capo_amp.types.rule_groups_namespace_status.RuleGroupsNamespaceStatus"
    """<p>A structure that returns the current status of the rule groups namespace.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>The list of tag keys and values that are associated with the namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleGroupsNamespaceResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    import capo_amp.types.rule_groups_namespace_status

    out["status"] = capo_amp.types.rule_groups_namespace_status.serialize_json(
        value["status"]
    )
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRuleGroupsNamespaceResponse:
    out: CreateRuleGroupsNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRuleGroupsNamespaceResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateRuleGroupsNamespaceResponse.arn required")
    if "status" in data:
        import capo_amp.types.rule_groups_namespace_status

        out["status"] = capo_amp.types.rule_groups_namespace_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateRuleGroupsNamespaceResponse.status required")
    if "tags" in data:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    return out
