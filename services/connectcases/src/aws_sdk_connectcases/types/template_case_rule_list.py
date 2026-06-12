"""Generated from Smithy shape ``com.amazonaws.connectcases#TemplateCaseRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.template_rule

TemplateCaseRuleList: TypeAlias = list[
    "aws_sdk_connectcases.types.template_rule.TemplateRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateCaseRuleList) -> list:
    import aws_sdk_connectcases.types.template_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.template_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> TemplateCaseRuleList:
    import aws_sdk_connectcases.types.template_rule

    out: TemplateCaseRuleList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.template_rule.deserialize_json(item))
    return out
