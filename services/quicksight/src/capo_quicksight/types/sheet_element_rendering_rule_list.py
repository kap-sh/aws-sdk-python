"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetElementRenderingRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_element_rendering_rule

SheetElementRenderingRuleList: TypeAlias = list[
    "capo_quicksight.types.sheet_element_rendering_rule.SheetElementRenderingRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetElementRenderingRuleList) -> list:
    import capo_quicksight.types.sheet_element_rendering_rule

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.sheet_element_rendering_rule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SheetElementRenderingRuleList:
    import capo_quicksight.types.sheet_element_rendering_rule

    out: SheetElementRenderingRuleList = []
    for item in data:
        out.append(
            capo_quicksight.types.sheet_element_rendering_rule.deserialize_json(item)
        )
    return out
