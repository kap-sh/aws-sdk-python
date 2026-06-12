"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#RealtimeContactAnalysisSegments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segment

RealtimeContactAnalysisSegments: TypeAlias = list[
    "aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segment.RealtimeContactAnalysisSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealtimeContactAnalysisSegments) -> list:
    import aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segment.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealtimeContactAnalysisSegments:
    import aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segment

    out: RealtimeContactAnalysisSegments = []
    for item in data:
        out.append(
            aws_sdk_connect_contact_lens.types.realtime_contact_analysis_segment.deserialize_json(
                item
            )
        )
    return out
