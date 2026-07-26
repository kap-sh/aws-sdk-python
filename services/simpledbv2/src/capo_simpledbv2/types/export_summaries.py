"""Generated from Smithy shape ``com.amazonaws.simpledbv2#ExportSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_simpledbv2.types.export_summary

ExportSummaries: TypeAlias = list["capo_simpledbv2.types.export_summary.ExportSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportSummaries) -> list:
    import capo_simpledbv2.types.export_summary

    out: list = []
    for item in value:
        out.append(capo_simpledbv2.types.export_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportSummaries:
    import capo_simpledbv2.types.export_summary

    out: ExportSummaries = []
    for item in data:
        out.append(capo_simpledbv2.types.export_summary.deserialize_json(item))
    return out
