"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemsFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_related_items_filter

OpsItemRelatedItemsFilters: TypeAlias = list[
    "capo_ssm.types.ops_item_related_items_filter.OpsItemRelatedItemsFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemRelatedItemsFilters) -> list:
    import capo_ssm.types.ops_item_related_items_filter

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.ops_item_related_items_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OpsItemRelatedItemsFilters:
    import capo_ssm.types.ops_item_related_items_filter

    out: OpsItemRelatedItemsFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.ops_item_related_items_filter.deserialize_aws_json_1_1(item)
        )
    return out
