"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.template_alias

TemplateAliasList: TypeAlias = list[
    "capo_quicksight.types.template_alias.TemplateAlias"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateAliasList) -> list:
    import capo_quicksight.types.template_alias

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.template_alias.serialize_json(item))
    return out


def deserialize_json(data: list) -> TemplateAliasList:
    import capo_quicksight.types.template_alias

    out: TemplateAliasList = []
    for item in data:
        out.append(capo_quicksight.types.template_alias.deserialize_json(item))
    return out
