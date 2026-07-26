"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#LinearRingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.linear_rings

LinearRingsList: TypeAlias = list[
    "capo_sagemaker_geospatial.types.linear_rings.LinearRings"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinearRingsList) -> list:
    import capo_sagemaker_geospatial.types.linear_rings

    out: list = []
    for item in value:
        out.append(capo_sagemaker_geospatial.types.linear_rings.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinearRingsList:
    import capo_sagemaker_geospatial.types.linear_rings

    out: LinearRingsList = []
    for item in data:
        out.append(capo_sagemaker_geospatial.types.linear_rings.deserialize_json(item))
    return out
