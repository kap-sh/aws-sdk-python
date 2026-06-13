"""Generated from Smithy shape ``com.amazonaws.inspector2#RuleSetCategories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.rule_set_category

RuleSetCategories: TypeAlias = list[
    "aws_sdk_inspector2.types.rule_set_category.RuleSetCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleSetCategories) -> list:
    import aws_sdk_inspector2.types.rule_set_category

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.rule_set_category.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleSetCategories:
    import aws_sdk_inspector2.types.rule_set_category

    out: RuleSetCategories = []
    for item in data:
        out.append(aws_sdk_inspector2.types.rule_set_category.deserialize_json(item))
    return out
