"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListSourceRepositoriesItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.list_source_repositories_item

ListSourceRepositoriesItems: TypeAlias = list[
    "aws_sdk_codecatalyst.types.list_source_repositories_item.ListSourceRepositoriesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceRepositoriesItems) -> list:
    import aws_sdk_codecatalyst.types.list_source_repositories_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecatalyst.types.list_source_repositories_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListSourceRepositoriesItems:
    import aws_sdk_codecatalyst.types.list_source_repositories_item

    out: ListSourceRepositoriesItems = []
    for item in data:
        out.append(
            aws_sdk_codecatalyst.types.list_source_repositories_item.deserialize_json(
                item
            )
        )
    return out
