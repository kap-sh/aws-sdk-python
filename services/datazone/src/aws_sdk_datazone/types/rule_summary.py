"""Generated from Smithy shape ``com.amazonaws.datazone#RuleSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.rule_action
    import aws_sdk_datazone.types.rule_id
    import aws_sdk_datazone.types.rule_name
    import aws_sdk_datazone.types.rule_scope
    import aws_sdk_datazone.types.rule_target
    import aws_sdk_datazone.types.rule_target_type
    import aws_sdk_datazone.types.rule_type
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class RuleSummary(TypedDict):
    identifier: NotRequired["aws_sdk_datazone.types.rule_id.RuleId"]
    """<p>The ID of the rule.</p>"""
    revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the rule.</p>"""
    rule_type: NotRequired["aws_sdk_datazone.types.rule_type.RuleType"]
    """<p>The type of the rule.</p>"""
    name: NotRequired["aws_sdk_datazone.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    target_type: NotRequired["aws_sdk_datazone.types.rule_target_type.RuleTargetType"]
    """<p>The target type of the rule.</p>"""
    target: NotRequired["aws_sdk_datazone.types.rule_target.RuleTarget"]
    """<p>The target of the rule.</p>"""
    action: NotRequired["aws_sdk_datazone.types.rule_action.RuleAction"]
    """<p>The action of the rule.</p>"""
    scope: NotRequired["aws_sdk_datazone.types.rule_scope.RuleScope"]
    """<p>The scope of the rule.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the rule was last updated.</p>"""
    last_updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The timestamp at which the rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleSummary) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "rule_type" in value:
        import aws_sdk_datazone.types.rule_type

        out["ruleType"] = aws_sdk_datazone.types.rule_type.serialize_json(
            value["rule_type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "target_type" in value:
        import aws_sdk_datazone.types.rule_target_type

        out["targetType"] = aws_sdk_datazone.types.rule_target_type.serialize_json(
            value["target_type"]
        )
    if "target" in value:
        import aws_sdk_datazone.types.rule_target

        out["target"] = aws_sdk_datazone.types.rule_target.serialize_json(
            value["target"]
        )
    if "action" in value:
        import aws_sdk_datazone.types.rule_action

        out["action"] = aws_sdk_datazone.types.rule_action.serialize_json(
            value["action"]
        )
    if "scope" in value:
        import aws_sdk_datazone.types.rule_scope

        out["scope"] = aws_sdk_datazone.types.rule_scope.serialize_json(value["scope"])
    if "updated_at" in value:
        import aws_sdk_datazone.types.updated_at

        out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    return out


def deserialize_json(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    if "revision" in data:
        out["revision"] = data["revision"]
    if "ruleType" in data:
        import aws_sdk_datazone.types.rule_type

        out["rule_type"] = aws_sdk_datazone.types.rule_type.deserialize_json(
            data["ruleType"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "targetType" in data:
        import aws_sdk_datazone.types.rule_target_type

        out["target_type"] = aws_sdk_datazone.types.rule_target_type.deserialize_json(
            data["targetType"]
        )
    if "target" in data:
        import aws_sdk_datazone.types.rule_target

        out["target"] = aws_sdk_datazone.types.rule_target.deserialize_json(
            data["target"]
        )
    if "action" in data:
        import aws_sdk_datazone.types.rule_action

        out["action"] = aws_sdk_datazone.types.rule_action.deserialize_json(
            data["action"]
        )
    if "scope" in data:
        import aws_sdk_datazone.types.rule_scope

        out["scope"] = aws_sdk_datazone.types.rule_scope.deserialize_json(data["scope"])
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    return out
