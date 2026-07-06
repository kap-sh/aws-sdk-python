"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.rule_detail
    import aws_sdk_datazone.types.rule_id
    import aws_sdk_datazone.types.rule_name
    import aws_sdk_datazone.types.rule_scope


class UpdateRuleInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which a rule is to be updated.</p>"""
    identifier: "aws_sdk_datazone.types.rule_id.RuleId"
    """<p>The ID of the rule that is to be updated</p>"""
    name: NotRequired["aws_sdk_datazone.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the rule.</p>"""
    scope: NotRequired["aws_sdk_datazone.types.rule_scope.RuleScope"]
    """<p>The scrope of the rule.</p>"""
    detail: NotRequired["aws_sdk_datazone.types.rule_detail.RuleDetail"]
    """<p>The detail of the rule.</p>"""
    include_child_domain_units: NotRequired["bool"]
    """<p>Specifies whether to update this rule in the child domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuleInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "scope" in value:
        import aws_sdk_datazone.types.rule_scope

        out["scope"] = aws_sdk_datazone.types.rule_scope.serialize_json(value["scope"])
    if "detail" in value:
        import aws_sdk_datazone.types.rule_detail

        out["detail"] = aws_sdk_datazone.types.rule_detail.serialize_json(
            value["detail"]
        )
    if "include_child_domain_units" in value:
        out["includeChildDomainUnits"] = value["include_child_domain_units"]
    return out


def deserialize_json(data: dict) -> UpdateRuleInput:
    out: UpdateRuleInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "scope" in data:
        import aws_sdk_datazone.types.rule_scope

        out["scope"] = aws_sdk_datazone.types.rule_scope.deserialize_json(data["scope"])
    if "detail" in data:
        import aws_sdk_datazone.types.rule_detail

        out["detail"] = aws_sdk_datazone.types.rule_detail.deserialize_json(
            data["detail"]
        )
    if "includeChildDomainUnits" in data:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    return out
