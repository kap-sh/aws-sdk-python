"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.workspace_search_criteria

WorkspaceSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.workspace_search_criteria.WorkspaceSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSearchConditionList) -> list:
    import aws_sdk_connect.types.workspace_search_criteria

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.workspace_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkspaceSearchConditionList:
    import aws_sdk_connect.types.workspace_search_criteria

    out: WorkspaceSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.workspace_search_criteria.deserialize_json(item)
        )
    return out
