"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FilterDimensionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.filter_dimension

FilterDimensionList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.filter_dimension.FilterDimension"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterDimensionList) -> list:
    import aws_sdk_customer_profiles.types.filter_dimension

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.filter_dimension.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FilterDimensionList:
    import aws_sdk_customer_profiles.types.filter_dimension

    out: FilterDimensionList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.filter_dimension.deserialize_json(item)
        )
    return out
