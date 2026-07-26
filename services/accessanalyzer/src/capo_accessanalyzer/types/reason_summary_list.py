"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ReasonSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.reason_summary

ReasonSummaryList: TypeAlias = list[
    "capo_accessanalyzer.types.reason_summary.ReasonSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReasonSummaryList) -> list:
    import capo_accessanalyzer.types.reason_summary

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.reason_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReasonSummaryList:
    import capo_accessanalyzer.types.reason_summary

    out: ReasonSummaryList = []
    for item in data:
        out.append(capo_accessanalyzer.types.reason_summary.deserialize_json(item))
    return out
