"""Generated from Smithy shape ``com.amazonaws.quicksight#GeocodePreferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geocode_preference

GeocodePreferenceList: TypeAlias = list[
    "aws_sdk_quicksight.types.geocode_preference.GeocodePreference"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeocodePreferenceList) -> list:
    import aws_sdk_quicksight.types.geocode_preference

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.geocode_preference.serialize_json(item))
    return out


def deserialize_json(data: list) -> GeocodePreferenceList:
    import aws_sdk_quicksight.types.geocode_preference

    out: GeocodePreferenceList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.geocode_preference.deserialize_json(item))
    return out
