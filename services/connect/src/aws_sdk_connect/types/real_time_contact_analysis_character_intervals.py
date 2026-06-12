"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisCharacterIntervals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_character_interval

RealTimeContactAnalysisCharacterIntervals: TypeAlias = list[
    "aws_sdk_connect.types.real_time_contact_analysis_character_interval.RealTimeContactAnalysisCharacterInterval"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisCharacterIntervals) -> list:
    import aws_sdk_connect.types.real_time_contact_analysis_character_interval

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.real_time_contact_analysis_character_interval.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealTimeContactAnalysisCharacterIntervals:
    import aws_sdk_connect.types.real_time_contact_analysis_character_interval

    out: RealTimeContactAnalysisCharacterIntervals = []
    for item in data:
        out.append(
            aws_sdk_connect.types.real_time_contact_analysis_character_interval.deserialize_json(
                item
            )
        )
    return out
