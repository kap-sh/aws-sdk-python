"""Generated from Smithy shape ``com.amazonaws.budgets#CostFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_budgets.types.dimension_values
    import aws_sdk_budgets.types.generic_string

CostFilters: TypeAlias = dict[
    "aws_sdk_budgets.types.generic_string.GenericString",
    "aws_sdk_budgets.types.dimension_values.DimensionValues",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CostFilters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_budgets.types.dimension_values

        out[key] = aws_sdk_budgets.types.dimension_values.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> CostFilters:
    out: CostFilters = {}
    for key, value in data.items():
        import aws_sdk_budgets.types.dimension_values

        out[key] = aws_sdk_budgets.types.dimension_values.deserialize_aws_json_1_1(
            value
        )
    return out
