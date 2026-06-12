"""Generated from Smithy shape ``com.amazonaws.costexplorer#DimensionValuesWithAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.dimension_values_with_attributes

DimensionValuesWithAttributesList: TypeAlias = list[
    "aws_sdk_cost_explorer.types.dimension_values_with_attributes.DimensionValuesWithAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionValuesWithAttributesList) -> list:
    import aws_sdk_cost_explorer.types.dimension_values_with_attributes

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.dimension_values_with_attributes.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DimensionValuesWithAttributesList:
    import aws_sdk_cost_explorer.types.dimension_values_with_attributes

    out: DimensionValuesWithAttributesList = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.dimension_values_with_attributes.deserialize_aws_json_1_1(
                item
            )
        )
    return out
