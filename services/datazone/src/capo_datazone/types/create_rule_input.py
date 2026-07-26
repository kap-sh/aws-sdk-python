"""Generated from Smithy shape ``com.amazonaws.datazone#CreateRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.rule_action
    import capo_datazone.types.rule_detail
    import capo_datazone.types.rule_name
    import capo_datazone.types.rule_scope
    import capo_datazone.types.rule_target


class CreateRuleInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the rule is created.</p>"""
    name: "capo_datazone.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    target: "capo_datazone.types.rule_target.RuleTarget"
    """<p>The target of the rule.</p>"""
    action: "capo_datazone.types.rule_action.RuleAction"
    """<p>The action of the rule.</p>"""
    scope: "capo_datazone.types.rule_scope.RuleScope"
    """<p>The scope of the rule.</p>"""
    detail: "capo_datazone.types.rule_detail.RuleDetail"
    """<p>The detail of the rule.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the rule.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_datazone.types.rule_target

    out["target"] = capo_datazone.types.rule_target.serialize_json(value["target"])
    import capo_datazone.types.rule_action

    out["action"] = capo_datazone.types.rule_action.serialize_json(value["action"])
    import capo_datazone.types.rule_scope

    out["scope"] = capo_datazone.types.rule_scope.serialize_json(value["scope"])
    import capo_datazone.types.rule_detail

    out["detail"] = capo_datazone.types.rule_detail.serialize_json(value["detail"])
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
        import capo_datazone.types.rule_target

        out["target"] = capo_datazone.types.rule_target.deserialize_json(data["target"])
    else:
        raise DeserializationError("CreateRuleInput.target required")
    if "action" in data:
        import capo_datazone.types.rule_action

        out["action"] = capo_datazone.types.rule_action.deserialize_json(data["action"])
    else:
        raise DeserializationError("CreateRuleInput.action required")
    if "scope" in data:
        import capo_datazone.types.rule_scope

        out["scope"] = capo_datazone.types.rule_scope.deserialize_json(data["scope"])
    else:
        raise DeserializationError("CreateRuleInput.scope required")
    if "detail" in data:
        import capo_datazone.types.rule_detail

        out["detail"] = capo_datazone.types.rule_detail.deserialize_json(data["detail"])
    else:
        raise DeserializationError("CreateRuleInput.detail required")
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
