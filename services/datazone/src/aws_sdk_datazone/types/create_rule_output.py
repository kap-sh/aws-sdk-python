"""Generated from Smithy shape ``com.amazonaws.datazone#CreateRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.rule_action
    import aws_sdk_datazone.types.rule_detail
    import aws_sdk_datazone.types.rule_id
    import aws_sdk_datazone.types.rule_name
    import aws_sdk_datazone.types.rule_scope
    import aws_sdk_datazone.types.rule_target
    import aws_sdk_datazone.types.rule_target_type
    import aws_sdk_datazone.types.rule_type


class CreateRuleOutput(TypedDict, closed=True):
    identifier: "aws_sdk_datazone.types.rule_id.RuleId"
    """<p>The ID of the rule.</p>"""
    name: "aws_sdk_datazone.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    rule_type: "aws_sdk_datazone.types.rule_type.RuleType"
    """<p>The type of the rule.</p>"""
    target: "aws_sdk_datazone.types.rule_target.RuleTarget"
    """<p>The target of the rule.</p>"""
    action: "aws_sdk_datazone.types.rule_action.RuleAction"
    """<p>The action of the rule.</p>"""
    scope: "aws_sdk_datazone.types.rule_scope.RuleScope"
    """<p>The scope of the rule.</p>"""
    detail: "aws_sdk_datazone.types.rule_detail.RuleDetail"
    """<p>The detail of the rule.</p>"""
    target_type: NotRequired["aws_sdk_datazone.types.rule_target_type.RuleTargetType"]
    """<p>The target type of the rule.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the rule.</p>"""
    created_at: "aws_sdk_datazone.types.created_at.CreatedAt"
    """<p>The timestamp at which the rule is created.</p>"""
    created_by: "aws_sdk_datazone.types.created_by.CreatedBy"
    """<p>The user who creates the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleOutput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["name"] = value["name"]
    import aws_sdk_datazone.types.rule_type

    out["ruleType"] = aws_sdk_datazone.types.rule_type.serialize_json(
        value["rule_type"]
    )
    import aws_sdk_datazone.types.rule_target

    out["target"] = aws_sdk_datazone.types.rule_target.serialize_json(value["target"])
    import aws_sdk_datazone.types.rule_action

    out["action"] = aws_sdk_datazone.types.rule_action.serialize_json(value["action"])
    import aws_sdk_datazone.types.rule_scope

    out["scope"] = aws_sdk_datazone.types.rule_scope.serialize_json(value["scope"])
    import aws_sdk_datazone.types.rule_detail

    out["detail"] = aws_sdk_datazone.types.rule_detail.serialize_json(value["detail"])
    if "target_type" in value:
        import aws_sdk_datazone.types.rule_target_type

        out["targetType"] = aws_sdk_datazone.types.rule_target_type.serialize_json(
            value["target_type"]
        )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_datazone.types.created_at

    out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> CreateRuleOutput:
    out: CreateRuleOutput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("CreateRuleOutput.identifier required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRuleOutput.name required")
    if "ruleType" in data:
        import aws_sdk_datazone.types.rule_type

        out["rule_type"] = aws_sdk_datazone.types.rule_type.deserialize_json(
            data["ruleType"]
        )
    else:
        raise DeserializationError("CreateRuleOutput.rule_type required")
    if "target" in data:
        import aws_sdk_datazone.types.rule_target

        out["target"] = aws_sdk_datazone.types.rule_target.deserialize_json(
            data["target"]
        )
    else:
        raise DeserializationError("CreateRuleOutput.target required")
    if "action" in data:
        import aws_sdk_datazone.types.rule_action

        out["action"] = aws_sdk_datazone.types.rule_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("CreateRuleOutput.action required")
    if "scope" in data:
        import aws_sdk_datazone.types.rule_scope

        out["scope"] = aws_sdk_datazone.types.rule_scope.deserialize_json(data["scope"])
    else:
        raise DeserializationError("CreateRuleOutput.scope required")
    if "detail" in data:
        import aws_sdk_datazone.types.rule_detail

        out["detail"] = aws_sdk_datazone.types.rule_detail.deserialize_json(
            data["detail"]
        )
    else:
        raise DeserializationError("CreateRuleOutput.detail required")
    if "targetType" in data:
        import aws_sdk_datazone.types.rule_target_type

        out["target_type"] = aws_sdk_datazone.types.rule_target_type.deserialize_json(
            data["targetType"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateRuleOutput.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("CreateRuleOutput.created_by required")
    return out
