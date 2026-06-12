"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisPointsOfInterest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_point_of_interest

RealTimeContactAnalysisPointsOfInterest: TypeAlias = list[
    "aws_sdk_connect.types.real_time_contact_analysis_point_of_interest.RealTimeContactAnalysisPointOfInterest"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisPointsOfInterest) -> list:
    import aws_sdk_connect.types.real_time_contact_analysis_point_of_interest

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.real_time_contact_analysis_point_of_interest.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealTimeContactAnalysisPointsOfInterest:
    import aws_sdk_connect.types.real_time_contact_analysis_point_of_interest

    out: RealTimeContactAnalysisPointsOfInterest = []
    for item in data:
        out.append(
            aws_sdk_connect.types.real_time_contact_analysis_point_of_interest.deserialize_json(
                item
            )
        )
    return out
