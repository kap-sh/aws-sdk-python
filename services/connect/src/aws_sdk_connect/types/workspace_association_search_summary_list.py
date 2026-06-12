"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceAssociationSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.workspace_association_search_summary

WorkspaceAssociationSearchSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.workspace_association_search_summary.WorkspaceAssociationSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceAssociationSearchSummaryList) -> list:
    import aws_sdk_connect.types.workspace_association_search_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.workspace_association_search_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WorkspaceAssociationSearchSummaryList:
    import aws_sdk_connect.types.workspace_association_search_summary

    out: WorkspaceAssociationSearchSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.workspace_association_search_summary.deserialize_json(
                item
            )
        )
    return out
