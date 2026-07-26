"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#AreaOfInterest``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.area_of_interest_geometry


class _AreaOfInterest_AreaOfInterestGeometry(TypedDict, closed=True):
    AreaOfInterestGeometry: "capo_sagemaker_geospatial.types.area_of_interest_geometry.AreaOfInterestGeometry"


AreaOfInterest: TypeAlias = _AreaOfInterest_AreaOfInterestGeometry


# --- restJson1 ser/de ---
def serialize_json(value: AreaOfInterest) -> dict:
    if "AreaOfInterestGeometry" in value:
        import capo_sagemaker_geospatial.types.area_of_interest_geometry

        return {
            "AreaOfInterestGeometry": capo_sagemaker_geospatial.types.area_of_interest_geometry.serialize_json(
                value["AreaOfInterestGeometry"]
            )
        }
    else:
        raise SerializationError("AreaOfInterest: no variant present")


def deserialize_json(data: dict) -> AreaOfInterest:
    if "AreaOfInterestGeometry" in data:
        import capo_sagemaker_geospatial.types.area_of_interest_geometry

        return {
            "AreaOfInterestGeometry": capo_sagemaker_geospatial.types.area_of_interest_geometry.deserialize_json(
                data["AreaOfInterestGeometry"]
            )
        }
    else:
        raise DeserializationError("AreaOfInterest: no recognized variant key")
