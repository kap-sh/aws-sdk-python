"""Generated from Smithy shape ``com.amazonaws.datazone#CreateRuleInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.rule_action
    import aws_sdk_datazone.types.rule_detail
    import aws_sdk_datazone.types.rule_name
    import aws_sdk_datazone.types.rule_scope
    import aws_sdk_datazone.types.rule_target


class CreateRuleInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the rule is created.</p>"""
    name: "aws_sdk_datazone.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    target: "aws_sdk_datazone.types.rule_target.RuleTarget"
    """<p>The target of the rule.</p>"""
    action: "aws_sdk_datazone.types.rule_action.RuleAction"
    """<p>The action of the rule.</p>"""
    scope: "aws_sdk_datazone.types.rule_scope.RuleScope"
    """<p>The scope of the rule.</p>"""
    detail: "aws_sdk_datazone.types.rule_detail.RuleDetail"
    """<p>The detail of the rule.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the rule.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_datazone.types.rule_target

    out["target"] = aws_sdk_datazone.types.rule_target.serialize_json(value["target"])
    import aws_sdk_datazone.types.rule_action

    out["action"] = aws_sdk_datazone.types.rule_action.serialize_json(value["action"])
    import aws_sdk_datazone.types.rule_scope

    out["scope"] = aws_sdk_datazone.types.rule_scope.serialize_json(value["scope"])
    import aws_sdk_datazone.types.rule_detail

    out["detail"] = aws_sdk_datazone.types.rule_detail.serialize_json(value["detail"])
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRuleInput:
    out: CreateRuleInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRuleInput.name required")
    if "target" in data:
        import aws_sdk_datazone.types.rule_target

        out["target"] = aws_sdk_datazone.types.rule_target.deserialize_json(
            data["target"]
        )
    else:
        raise DeserializationError("CreateRuleInput.target required")
    if "action" in data:
        import aws_sdk_datazone.types.rule_action

        out["action"] = aws_sdk_datazone.types.rule_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("CreateRuleInput.action required")
    if "scope" in data:
        import aws_sdk_datazone.types.rule_scope

        out["scope"] = aws_sdk_datazone.types.rule_scope.deserialize_json(data["scope"])
    else:
        raise DeserializationError("CreateRuleInput.scope required")
    if "detail" in data:
        import aws_sdk_datazone.types.rule_detail

        out["detail"] = aws_sdk_datazone.types.rule_detail.deserialize_json(
            data["detail"]
        )
    else:
        raise DeserializationError("CreateRuleInput.detail required")
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
