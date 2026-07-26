"""Generated from Smithy shape ``com.amazonaws.datazone#GetRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.revision
    import capo_datazone.types.rule_action
    import capo_datazone.types.rule_detail
    import capo_datazone.types.rule_id
    import capo_datazone.types.rule_name
    import capo_datazone.types.rule_scope
    import capo_datazone.types.rule_target
    import capo_datazone.types.rule_target_type
    import capo_datazone.types.rule_type
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class GetRuleOutput(TypedDict, closed=True):
    identifier: "capo_datazone.types.rule_id.RuleId"
    """<p>The ID of the rule.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of the rule.</p>"""
    name: "capo_datazone.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    rule_type: "capo_datazone.types.rule_type.RuleType"
    """<p>The type of the rule.</p>"""
    target: "capo_datazone.types.rule_target.RuleTarget"
    """<p>The target of the rule.</p>"""
    action: "capo_datazone.types.rule_action.RuleAction"
    """<p>The action of the rule.</p>"""
    scope: "capo_datazone.types.rule_scope.RuleScope"
    """<p>The scope of the rule.</p>"""
    detail: "capo_datazone.types.rule_detail.RuleDetail"
    """<p>The detail of the rule.</p>"""
    target_type: NotRequired["capo_datazone.types.rule_target_type.RuleTargetType"]
    """<p>The target type of the rule.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the rule.</p>"""
    created_at: "capo_datazone.types.created_at.CreatedAt"
    """<p>The timestamp at which the rule was created.</p>"""
    updated_at: "capo_datazone.types.updated_at.UpdatedAt"
    """<p>The timestamp at which the rule was last updated.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The user who created the rule.</p>"""
    last_updated_by: "capo_datazone.types.updated_by.UpdatedBy"
    """<p>The timestamp at which the rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuleOutput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["revision"] = value["revision"]
    out["name"] = value["name"]
    import capo_datazone.types.rule_type

    out["ruleType"] = capo_datazone.types.rule_type.serialize_json(value["rule_type"])
    import capo_datazone.types.rule_target

    out["target"] = capo_datazone.types.rule_target.serialize_json(value["target"])
    import capo_datazone.types.rule_action

    out["action"] = capo_datazone.types.rule_action.serialize_json(value["action"])
    import capo_datazone.types.rule_scope

    out["scope"] = capo_datazone.types.rule_scope.serialize_json(value["scope"])
    import capo_datazone.types.rule_detail

    out["detail"] = capo_datazone.types.rule_detail.serialize_json(value["detail"])
    if "target_type" in value:
        import capo_datazone.types.rule_target_type

        out["targetType"] = capo_datazone.types.rule_target_type.serialize_json(
            value["target_type"]
        )
    if "description" in value:
        out["description"] = value["description"]
    import capo_datazone.types.created_at

    out["createdAt"] = capo_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    import capo_datazone.types.updated_at

    out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
        value["updated_at"]
    )
    out["createdBy"] = value["created_by"]
    out["lastUpdatedBy"] = value["last_updated_by"]
    return out


def deserialize_json(data: dict) -> GetRuleOutput:
    out: GetRuleOutput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("GetRuleOutput.identifier required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("GetRuleOutput.revision required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetRuleOutput.name required")
    if "ruleType" in data:
        import capo_datazone.types.rule_type

        out["rule_type"] = capo_datazone.types.rule_type.deserialize_json(
            data["ruleType"]
        )
    else:
        raise DeserializationError("GetRuleOutput.rule_type required")
    if "target" in data:
        import capo_datazone.types.rule_target

        out["target"] = capo_datazone.types.rule_target.deserialize_json(data["target"])
    else:
        raise DeserializationError("GetRuleOutput.target required")
    if "action" in data:
        import capo_datazone.types.rule_action

        out["action"] = capo_datazone.types.rule_action.deserialize_json(data["action"])
    else:
        raise DeserializationError("GetRuleOutput.action required")
    if "scope" in data:
        import capo_datazone.types.rule_scope

        out["scope"] = capo_datazone.types.rule_scope.deserialize_json(data["scope"])
    else:
        raise DeserializationError("GetRuleOutput.scope required")
    if "detail" in data:
        import capo_datazone.types.rule_detail

        out["detail"] = capo_datazone.types.rule_detail.deserialize_json(data["detail"])
    else:
        raise DeserializationError("GetRuleOutput.detail required")
    if "targetType" in data:
        import capo_datazone.types.rule_target_type

        out["target_type"] = capo_datazone.types.rule_target_type.deserialize_json(
            data["targetType"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetRuleOutput.created_at required")
    if "updatedAt" in data:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetRuleOutput.updated_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetRuleOutput.created_by required")
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    else:
        raise DeserializationError("GetRuleOutput.last_updated_by required")
    return out
