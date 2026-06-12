"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemsFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_related_items_filter_value

OpsItemRelatedItemsFilterValues: TypeAlias = list[
    "aws_sdk_ssm.types.ops_item_related_items_filter_value.OpsItemRelatedItemsFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemRelatedItemsFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OpsItemRelatedItemsFilterValues:
    return list(data)
