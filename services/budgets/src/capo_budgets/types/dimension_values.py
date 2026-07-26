"""Generated from Smithy shape ``com.amazonaws.budgets#DimensionValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.dimension_value

DimensionValues: TypeAlias = list["capo_budgets.types.dimension_value.DimensionValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DimensionValues:
    return list(data)
