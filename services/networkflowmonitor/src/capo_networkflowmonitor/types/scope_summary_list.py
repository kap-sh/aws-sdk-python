"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ScopeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.scope_summary

ScopeSummaryList: TypeAlias = list[
    "capo_networkflowmonitor.types.scope_summary.ScopeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeSummaryList) -> list:
    import capo_networkflowmonitor.types.scope_summary

    out: list = []
    for item in value:
        out.append(capo_networkflowmonitor.types.scope_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScopeSummaryList:
    import capo_networkflowmonitor.types.scope_summary

    out: ScopeSummaryList = []
    for item in data:
        out.append(capo_networkflowmonitor.types.scope_summary.deserialize_json(item))
    return out
