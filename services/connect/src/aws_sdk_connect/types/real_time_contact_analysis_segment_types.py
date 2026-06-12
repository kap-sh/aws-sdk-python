"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_segment_type

RealTimeContactAnalysisSegmentTypes: TypeAlias = list[
    "aws_sdk_connect.types.real_time_contact_analysis_segment_type.RealTimeContactAnalysisSegmentType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentTypes) -> list:
    import aws_sdk_connect.types.real_time_contact_analysis_segment_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.real_time_contact_analysis_segment_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealTimeContactAnalysisSegmentTypes:
    import aws_sdk_connect.types.real_time_contact_analysis_segment_type

    out: RealTimeContactAnalysisSegmentTypes = []
    for item in data:
        out.append(
            aws_sdk_connect.types.real_time_contact_analysis_segment_type.deserialize_json(
                item
            )
        )
    return out
