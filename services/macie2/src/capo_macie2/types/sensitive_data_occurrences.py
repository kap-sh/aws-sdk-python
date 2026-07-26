"""Generated from Smithy shape ``com.amazonaws.macie2#SensitiveDataOccurrences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_detected_data_details
    import capo_macie2.types.__string

SensitiveDataOccurrences: TypeAlias = dict[
    "capo_macie2.types.__string.__string",
    "capo_macie2.types.__list_of_detected_data_details.__listOfDetectedDataDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SensitiveDataOccurrences) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_macie2.types.__list_of_detected_data_details

        out[key] = capo_macie2.types.__list_of_detected_data_details.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> SensitiveDataOccurrences:
    out: SensitiveDataOccurrences = {}
    for key, value in data.items():
        import capo_macie2.types.__list_of_detected_data_details

        out[key] = capo_macie2.types.__list_of_detected_data_details.deserialize_json(
            value
        )
    return out
