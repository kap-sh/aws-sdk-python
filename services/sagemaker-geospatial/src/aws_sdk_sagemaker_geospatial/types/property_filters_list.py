"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#PropertyFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.property_filter

PropertyFiltersList: TypeAlias = list[
    "aws_sdk_sagemaker_geospatial.types.property_filter.PropertyFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyFiltersList) -> list:
    import aws_sdk_sagemaker_geospatial.types.property_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker_geospatial.types.property_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PropertyFiltersList:
    import aws_sdk_sagemaker_geospatial.types.property_filter

    out: PropertyFiltersList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker_geospatial.types.property_filter.deserialize_json(item)
        )
    return out
