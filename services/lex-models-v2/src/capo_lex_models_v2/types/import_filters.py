"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.import_filter

ImportFilters: TypeAlias = list["capo_lex_models_v2.types.import_filter.ImportFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportFilters) -> list:
    import capo_lex_models_v2.types.import_filter

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.import_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportFilters:
    import capo_lex_models_v2.types.import_filter

    out: ImportFilters = []
    for item in data:
        out.append(capo_lex_models_v2.types.import_filter.deserialize_json(item))
    return out
