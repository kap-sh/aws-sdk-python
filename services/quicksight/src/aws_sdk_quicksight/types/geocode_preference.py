"""Generated from Smithy shape ``com.amazonaws.quicksight#GeocodePreference``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geocode_preference_value
    import aws_sdk_quicksight.types.geocoder_hierarchy


class GeocodePreference(TypedDict):
    request_key: "aws_sdk_quicksight.types.geocoder_hierarchy.GeocoderHierarchy"
    """<p>The unique request key for the geocode preference.</p>"""
    preference: (
        "aws_sdk_quicksight.types.geocode_preference_value.GeocodePreferenceValue"
    )
    """<p>The preference definition for the geocode preference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeocodePreference) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.geocoder_hierarchy

    out["RequestKey"] = aws_sdk_quicksight.types.geocoder_hierarchy.serialize_json(
        value["request_key"]
    )
    import aws_sdk_quicksight.types.geocode_preference_value

    out["Preference"] = (
        aws_sdk_quicksight.types.geocode_preference_value.serialize_json(
            value["preference"]
        )
    )
    return out


def deserialize_json(data: dict) -> GeocodePreference:
    out: GeocodePreference = {}  # type: ignore[typeddict-item]
    if "RequestKey" in data:
        import aws_sdk_quicksight.types.geocoder_hierarchy

        out["request_key"] = (
            aws_sdk_quicksight.types.geocoder_hierarchy.deserialize_json(
                data["RequestKey"]
            )
        )
    else:
        raise DeserializationError("GeocodePreference.request_key required")
    if "Preference" in data:
        import aws_sdk_quicksight.types.geocode_preference_value

        out["preference"] = (
            aws_sdk_quicksight.types.geocode_preference_value.deserialize_json(
                data["Preference"]
            )
        )
    else:
        raise DeserializationError("GeocodePreference.preference required")
    return out
