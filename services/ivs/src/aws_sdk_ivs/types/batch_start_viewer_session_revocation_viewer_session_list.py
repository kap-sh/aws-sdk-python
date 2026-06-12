"""Generated from Smithy shape ``com.amazonaws.ivs#BatchStartViewerSessionRevocationViewerSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.batch_start_viewer_session_revocation_viewer_session

BatchStartViewerSessionRevocationViewerSessionList: TypeAlias = list[
    "aws_sdk_ivs.types.batch_start_viewer_session_revocation_viewer_session.BatchStartViewerSessionRevocationViewerSession"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchStartViewerSessionRevocationViewerSessionList) -> list:
    import aws_sdk_ivs.types.batch_start_viewer_session_revocation_viewer_session

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs.types.batch_start_viewer_session_revocation_viewer_session.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchStartViewerSessionRevocationViewerSessionList:
    import aws_sdk_ivs.types.batch_start_viewer_session_revocation_viewer_session

    out: BatchStartViewerSessionRevocationViewerSessionList = []
    for item in data:
        out.append(
            aws_sdk_ivs.types.batch_start_viewer_session_revocation_viewer_session.deserialize_json(
                item
            )
        )
    return out
