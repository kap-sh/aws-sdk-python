"""Generated from Smithy shape ``com.amazonaws.ssm#TerminateSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.session_id


class TerminateSessionResponse(TypedDict, closed=True):
    session_id: NotRequired["capo_ssm.types.session_id.SessionId"]
    """<p>The ID of the session that has been terminated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateSessionResponse) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateSessionResponse:
    out: TerminateSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    return out
