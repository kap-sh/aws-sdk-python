"""Generated from Smithy shape ``com.amazonaws.quicksight#GeocodePreferenceValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.coordinate
    import aws_sdk_quicksight.types.geocoder_hierarchy


class _GeocodePreferenceValue_GeocoderHierarchy(TypedDict):
    GeocoderHierarchy: "aws_sdk_quicksight.types.geocoder_hierarchy.GeocoderHierarchy"


class _GeocodePreferenceValue_Coordinate(TypedDict):
    Coordinate: "aws_sdk_quicksight.types.coordinate.Coordinate"


GeocodePreferenceValue: TypeAlias = (
    _GeocodePreferenceValue_GeocoderHierarchy | _GeocodePreferenceValue_Coordinate
)


# --- restJson1 ser/de ---
def serialize_json(value: GeocodePreferenceValue) -> dict:
    if "GeocoderHierarchy" in value:
        import aws_sdk_quicksight.types.geocoder_hierarchy

        return {
            "GeocoderHierarchy": aws_sdk_quicksight.types.geocoder_hierarchy.serialize_json(
                value["GeocoderHierarchy"]
            )
        }
    elif "Coordinate" in value:
        import aws_sdk_quicksight.types.coordinate

        return {
            "Coordinate": aws_sdk_quicksight.types.coordinate.serialize_json(
                value["Coordinate"]
            )
        }
    else:
        raise SerializationError("GeocodePreferenceValue: no variant present")


def deserialize_json(data: dict) -> GeocodePreferenceValue:
    if "GeocoderHierarchy" in data:
        import aws_sdk_quicksight.types.geocoder_hierarchy

        return {
            "GeocoderHierarchy": aws_sdk_quicksight.types.geocoder_hierarchy.deserialize_json(
                data["GeocoderHierarchy"]
            )
        }
    elif "Coordinate" in data:
        import aws_sdk_quicksight.types.coordinate

        return {
            "Coordinate": aws_sdk_quicksight.types.coordinate.deserialize_json(
                data["Coordinate"]
            )
        }
    else:
        raise DeserializationError("GeocodePreferenceValue: no recognized variant key")
