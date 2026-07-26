"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.finding_summary

FindingsList: TypeAlias = list[
    "capo_accessanalyzer.types.finding_summary.FindingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsList) -> list:
    import capo_accessanalyzer.types.finding_summary

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.finding_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingsList:
    import capo_accessanalyzer.types.finding_summary

    out: FindingsList = []
    for item in data:
        out.append(capo_accessanalyzer.types.finding_summary.deserialize_json(item))
    return out
