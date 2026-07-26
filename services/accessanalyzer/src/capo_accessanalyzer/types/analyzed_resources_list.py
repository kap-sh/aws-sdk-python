"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalyzedResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzed_resource_summary

AnalyzedResourcesList: TypeAlias = list[
    "capo_accessanalyzer.types.analyzed_resource_summary.AnalyzedResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzedResourcesList) -> list:
    import capo_accessanalyzer.types.analyzed_resource_summary

    out: list = []
    for item in value:
        out.append(
            capo_accessanalyzer.types.analyzed_resource_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyzedResourcesList:
    import capo_accessanalyzer.types.analyzed_resource_summary

    out: AnalyzedResourcesList = []
    for item in data:
        out.append(
            capo_accessanalyzer.types.analyzed_resource_summary.deserialize_json(item)
        )
    return out
