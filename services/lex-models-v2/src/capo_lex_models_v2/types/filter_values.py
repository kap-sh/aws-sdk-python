"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#FilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.filter_value

FilterValues: TypeAlias = list["capo_lex_models_v2.types.filter_value.FilterValue"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterValues:
    return list(data)
