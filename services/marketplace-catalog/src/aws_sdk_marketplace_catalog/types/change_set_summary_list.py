"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ChangeSetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.change_set_summary_list_item

ChangeSetSummaryList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.change_set_summary_list_item.ChangeSetSummaryListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeSetSummaryList) -> list:
    import aws_sdk_marketplace_catalog.types.change_set_summary_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_catalog.types.change_set_summary_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChangeSetSummaryList:
    import aws_sdk_marketplace_catalog.types.change_set_summary_list_item

    out: ChangeSetSummaryList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_catalog.types.change_set_summary_list_item.deserialize_json(
                item
            )
        )
    return out
