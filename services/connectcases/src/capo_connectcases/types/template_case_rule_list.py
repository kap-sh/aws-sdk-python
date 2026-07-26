"""Generated from Smithy shape ``com.amazonaws.connectcases#TemplateCaseRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.template_rule

TemplateCaseRuleList: TypeAlias = list[
    "capo_connectcases.types.template_rule.TemplateRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateCaseRuleList) -> list:
    import capo_connectcases.types.template_rule

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.template_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> TemplateCaseRuleList:
    import capo_connectcases.types.template_rule

    out: TemplateCaseRuleList = []
    for item in data:
        out.append(capo_connectcases.types.template_rule.deserialize_json(item))
    return out
