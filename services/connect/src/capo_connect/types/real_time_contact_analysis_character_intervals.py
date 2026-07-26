"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisCharacterIntervals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_character_interval

RealTimeContactAnalysisCharacterIntervals: TypeAlias = list[
    "capo_connect.types.real_time_contact_analysis_character_interval.RealTimeContactAnalysisCharacterInterval"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisCharacterIntervals) -> list:
    import capo_connect.types.real_time_contact_analysis_character_interval

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.real_time_contact_analysis_character_interval.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealTimeContactAnalysisCharacterIntervals:
    import capo_connect.types.real_time_contact_analysis_character_interval

    out: RealTimeContactAnalysisCharacterIntervals = []
    for item in data:
        out.append(
            capo_connect.types.real_time_contact_analysis_character_interval.deserialize_json(
                item
            )
        )
    return out
