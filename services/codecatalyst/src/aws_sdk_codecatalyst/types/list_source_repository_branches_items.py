"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListSourceRepositoryBranchesItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.list_source_repository_branches_item

ListSourceRepositoryBranchesItems: TypeAlias = list[
    "aws_sdk_codecatalyst.types.list_source_repository_branches_item.ListSourceRepositoryBranchesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceRepositoryBranchesItems) -> list:
    import aws_sdk_codecatalyst.types.list_source_repository_branches_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecatalyst.types.list_source_repository_branches_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListSourceRepositoryBranchesItems:
    import aws_sdk_codecatalyst.types.list_source_repository_branches_item

    out: ListSourceRepositoryBranchesItems = []
    for item in data:
        out.append(
            aws_sdk_codecatalyst.types.list_source_repository_branches_item.deserialize_json(
                item
            )
        )
    return out
