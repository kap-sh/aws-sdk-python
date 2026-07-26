"""Generated from Smithy shape ``com.amazonaws.inspector2#RuleSetCategories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.rule_set_category

RuleSetCategories: TypeAlias = list[
    "capo_inspector2.types.rule_set_category.RuleSetCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleSetCategories) -> list:
    import capo_inspector2.types.rule_set_category

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.rule_set_category.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleSetCategories:
    import capo_inspector2.types.rule_set_category

    out: RuleSetCategories = []
    for item in data:
        out.append(capo_inspector2.types.rule_set_category.deserialize_json(item))
    return out
