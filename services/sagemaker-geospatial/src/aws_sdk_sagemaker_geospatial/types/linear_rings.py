"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#LinearRings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.linear_ring

LinearRings: TypeAlias = list[
    "aws_sdk_sagemaker_geospatial.types.linear_ring.LinearRing"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinearRings) -> list:
    import aws_sdk_sagemaker_geospatial.types.linear_ring

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker_geospatial.types.linear_ring.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinearRings:
    import aws_sdk_sagemaker_geospatial.types.linear_ring

    out: LinearRings = []
    for item in data:
        out.append(
            aws_sdk_sagemaker_geospatial.types.linear_ring.deserialize_json(item)
        )
    return out
