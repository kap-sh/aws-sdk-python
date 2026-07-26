"""Generated from Smithy shape ``com.amazonaws.ivs#BatchStartViewerSessionRevocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.batch_start_viewer_session_revocation_viewer_session_list


class BatchStartViewerSessionRevocationRequest(TypedDict, closed=True):
    viewer_sessions: "capo_ivs.types.batch_start_viewer_session_revocation_viewer_session_list.BatchStartViewerSessionRevocationViewerSessionList"
    """<p>Array of viewer sessions, one per channel-ARN and viewer-ID pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchStartViewerSessionRevocationRequest) -> dict:
    out: dict = {}
    import capo_ivs.types.batch_start_viewer_session_revocation_viewer_session_list

    out["viewerSessions"] = (
        capo_ivs.types.batch_start_viewer_session_revocation_viewer_session_list.serialize_json(
            value["viewer_sessions"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchStartViewerSessionRevocationRequest:
    out: BatchStartViewerSessionRevocationRequest = {}  # type: ignore[typeddict-item]
    if "viewerSessions" in data:
        import capo_ivs.types.batch_start_viewer_session_revocation_viewer_session_list

        out["viewer_sessions"] = (
            capo_ivs.types.batch_start_viewer_session_revocation_viewer_session_list.deserialize_json(
                data["viewerSessions"]
            )
        )
    else:
        raise DeserializationError(
            "BatchStartViewerSessionRevocationRequest.viewer_sessions required"
        )
    return out
