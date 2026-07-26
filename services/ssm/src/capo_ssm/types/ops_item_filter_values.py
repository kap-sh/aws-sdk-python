"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_filter_value

OpsItemFilterValues: TypeAlias = list[
    "capo_ssm.types.ops_item_filter_value.OpsItemFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OpsItemFilterValues:
    return list(data)
