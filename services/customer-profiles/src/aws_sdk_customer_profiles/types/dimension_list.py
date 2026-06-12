"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DimensionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.dimension

DimensionList: TypeAlias = list["aws_sdk_customer_profiles.types.dimension.Dimension"]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionList) -> list:
    import aws_sdk_customer_profiles.types.dimension

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.dimension.serialize_json(item))
    return out


def deserialize_json(data: list) -> DimensionList:
    import aws_sdk_customer_profiles.types.dimension

    out: DimensionList = []
    for item in data:
        out.append(aws_sdk_customer_profiles.types.dimension.deserialize_json(item))
    return out
