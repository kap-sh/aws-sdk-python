"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.import_summary

ImportSummaryList: TypeAlias = list[
    "capo_lex_models_v2.types.import_summary.ImportSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportSummaryList) -> list:
    import capo_lex_models_v2.types.import_summary

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.import_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportSummaryList:
    import capo_lex_models_v2.types.import_summary

    out: ImportSummaryList = []
    for item in data:
        out.append(capo_lex_models_v2.types.import_summary.deserialize_json(item))
    return out
