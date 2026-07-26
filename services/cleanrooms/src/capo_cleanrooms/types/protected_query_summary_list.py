"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQuerySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query_summary

ProtectedQuerySummaryList: TypeAlias = list[
    "capo_cleanrooms.types.protected_query_summary.ProtectedQuerySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQuerySummaryList) -> list:
    import capo_cleanrooms.types.protected_query_summary

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.protected_query_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProtectedQuerySummaryList:
    import capo_cleanrooms.types.protected_query_summary

    out: ProtectedQuerySummaryList = []
    for item in data:
        out.append(capo_cleanrooms.types.protected_query_summary.deserialize_json(item))
    return out
