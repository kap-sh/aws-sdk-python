"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfDetectedDataDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.detected_data_details

__listOfDetectedDataDetails: TypeAlias = list[
    "capo_macie2.types.detected_data_details.DetectedDataDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDetectedDataDetails) -> list:
    import capo_macie2.types.detected_data_details

    out: list = []
    for item in value:
        out.append(capo_macie2.types.detected_data_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDetectedDataDetails:
    import capo_macie2.types.detected_data_details

    out: __listOfDetectedDataDetails = []
    for item in data:
        out.append(capo_macie2.types.detected_data_details.deserialize_json(item))
    return out
