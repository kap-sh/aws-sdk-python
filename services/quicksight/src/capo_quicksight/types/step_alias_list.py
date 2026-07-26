"""Generated from Smithy shape ``com.amazonaws.quicksight#StepAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.step_alias_mapping

StepAliasList: TypeAlias = list[
    "capo_quicksight.types.step_alias_mapping.StepAliasMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: StepAliasList) -> list:
    import capo_quicksight.types.step_alias_mapping

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.step_alias_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepAliasList:
    import capo_quicksight.types.step_alias_mapping

    out: StepAliasList = []
    for item in data:
        out.append(capo_quicksight.types.step_alias_mapping.deserialize_json(item))
    return out
