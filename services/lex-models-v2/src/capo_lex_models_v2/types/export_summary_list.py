"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.export_summary

ExportSummaryList: TypeAlias = list[
    "capo_lex_models_v2.types.export_summary.ExportSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportSummaryList) -> list:
    import capo_lex_models_v2.types.export_summary

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.export_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportSummaryList:
    import capo_lex_models_v2.types.export_summary

    out: ExportSummaryList = []
    for item in data:
        out.append(capo_lex_models_v2.types.export_summary.deserialize_json(item))
    return out
