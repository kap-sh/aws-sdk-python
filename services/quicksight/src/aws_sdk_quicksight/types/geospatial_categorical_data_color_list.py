"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialCategoricalDataColorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_categorical_data_color

GeospatialCategoricalDataColorList: TypeAlias = list[
    "aws_sdk_quicksight.types.geospatial_categorical_data_color.GeospatialCategoricalDataColor"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialCategoricalDataColorList) -> list:
    import aws_sdk_quicksight.types.geospatial_categorical_data_color

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.geospatial_categorical_data_color.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GeospatialCategoricalDataColorList:
    import aws_sdk_quicksight.types.geospatial_categorical_data_color

    out: GeospatialCategoricalDataColorList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.geospatial_categorical_data_color.deserialize_json(
                item
            )
        )
    return out
