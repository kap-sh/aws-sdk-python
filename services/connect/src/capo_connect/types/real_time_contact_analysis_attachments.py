"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisAttachments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_attachment

RealTimeContactAnalysisAttachments: TypeAlias = list[
    "capo_connect.types.real_time_contact_analysis_attachment.RealTimeContactAnalysisAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisAttachments) -> list:
    import capo_connect.types.real_time_contact_analysis_attachment

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.real_time_contact_analysis_attachment.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealTimeContactAnalysisAttachments:
    import capo_connect.types.real_time_contact_analysis_attachment

    out: RealTimeContactAnalysisAttachments = []
    for item in data:
        out.append(
            capo_connect.types.real_time_contact_analysis_attachment.deserialize_json(
                item
            )
        )
    return out
