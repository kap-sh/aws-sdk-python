"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.filter

FilterList: TypeAlias = list["aws_sdk_sagemaker_geospatial.types.filter.Filter"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterList) -> list:
    import aws_sdk_sagemaker_geospatial.types.filter

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker_geospatial.types.filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterList:
    import aws_sdk_sagemaker_geospatial.types.filter

    out: FilterList = []
    for item in data:
        out.append(aws_sdk_sagemaker_geospatial.types.filter.deserialize_json(item))
    return out
