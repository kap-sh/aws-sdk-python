"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceAssociationSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.workspace_association_search_criteria

WorkspaceAssociationSearchConditionList: TypeAlias = list[
    "capo_connect.types.workspace_association_search_criteria.WorkspaceAssociationSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceAssociationSearchConditionList) -> list:
    import capo_connect.types.workspace_association_search_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.workspace_association_search_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WorkspaceAssociationSearchConditionList:
    import capo_connect.types.workspace_association_search_criteria

    out: WorkspaceAssociationSearchConditionList = []
    for item in data:
        out.append(
            capo_connect.types.workspace_association_search_criteria.deserialize_json(
                item
            )
        )
    return out
