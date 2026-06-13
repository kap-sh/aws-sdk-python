"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#LinearRingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.linear_rings

LinearRingsList: TypeAlias = list[
    "aws_sdk_sagemaker_geospatial.types.linear_rings.LinearRings"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinearRingsList) -> list:
    import aws_sdk_sagemaker_geospatial.types.linear_rings

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker_geospatial.types.linear_rings.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinearRingsList:
    import aws_sdk_sagemaker_geospatial.types.linear_rings

    out: LinearRingsList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker_geospatial.types.linear_rings.deserialize_json(item)
        )
    return out
