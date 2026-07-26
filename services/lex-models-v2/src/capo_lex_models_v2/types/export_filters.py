"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.export_filter

ExportFilters: TypeAlias = list["capo_lex_models_v2.types.export_filter.ExportFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportFilters) -> list:
    import capo_lex_models_v2.types.export_filter

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.export_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportFilters:
    import capo_lex_models_v2.types.export_filter

    out: ExportFilters = []
    for item in data:
        out.append(capo_lex_models_v2.types.export_filter.deserialize_json(item))
    return out
