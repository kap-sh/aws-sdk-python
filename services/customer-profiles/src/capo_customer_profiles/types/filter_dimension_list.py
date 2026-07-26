"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FilterDimensionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.filter_dimension

FilterDimensionList: TypeAlias = list[
    "capo_customer_profiles.types.filter_dimension.FilterDimension"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterDimensionList) -> list:
    import capo_customer_profiles.types.filter_dimension

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.filter_dimension.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterDimensionList:
    import capo_customer_profiles.types.filter_dimension

    out: FilterDimensionList = []
    for item in data:
        out.append(capo_customer_profiles.types.filter_dimension.deserialize_json(item))
    return out
