"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.workspace_search_summary

WorkspaceSearchSummaryList: TypeAlias = list[
    "capo_connect.types.workspace_search_summary.WorkspaceSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSearchSummaryList) -> list:
    import capo_connect.types.workspace_search_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.workspace_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkspaceSearchSummaryList:
    import capo_connect.types.workspace_search_summary

    out: WorkspaceSearchSummaryList = []
    for item in data:
        out.append(capo_connect.types.workspace_search_summary.deserialize_json(item))
    return out
