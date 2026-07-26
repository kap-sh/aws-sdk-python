"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceAssociationSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.workspace_association_search_summary

WorkspaceAssociationSearchSummaryList: TypeAlias = list[
    "capo_connect.types.workspace_association_search_summary.WorkspaceAssociationSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceAssociationSearchSummaryList) -> list:
    import capo_connect.types.workspace_association_search_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.workspace_association_search_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkspaceAssociationSearchSummaryList:
    import capo_connect.types.workspace_association_search_summary

    out: WorkspaceAssociationSearchSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.workspace_association_search_summary.deserialize_json(
                item
            )
        )
    return out
