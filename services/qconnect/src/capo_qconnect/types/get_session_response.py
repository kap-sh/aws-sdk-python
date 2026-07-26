"""Generated from Smithy shape ``com.amazonaws.qconnect#GetSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.session_data


class GetSessionResponse(TypedDict, closed=True):
    session: NotRequired["capo_qconnect.types.session_data.SessionData"]
    """<p>The session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponse) -> dict:
    out: dict = {}
    if "session" in value:
        import capo_qconnect.types.session_data

        out["session"] = capo_qconnect.types.session_data.serialize_json(
            value["session"]
        )
    return out


def deserialize_json(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if "session" in data:
        import capo_qconnect.types.session_data

        out["session"] = capo_qconnect.types.session_data.deserialize_json(
            data["session"]
        )
    return out
