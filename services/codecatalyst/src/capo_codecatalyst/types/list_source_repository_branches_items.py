"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListSourceRepositoryBranchesItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.list_source_repository_branches_item

ListSourceRepositoryBranchesItems: TypeAlias = list[
    "capo_codecatalyst.types.list_source_repository_branches_item.ListSourceRepositoryBranchesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceRepositoryBranchesItems) -> list:
    import capo_codecatalyst.types.list_source_repository_branches_item

    out: list = []
    for item in value:
        out.append(
            capo_codecatalyst.types.list_source_repository_branches_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListSourceRepositoryBranchesItems:
    import capo_codecatalyst.types.list_source_repository_branches_item

    out: ListSourceRepositoryBranchesItems = []
    for item in data:
        out.append(
            capo_codecatalyst.types.list_source_repository_branches_item.deserialize_json(
                item
            )
        )
    return out
