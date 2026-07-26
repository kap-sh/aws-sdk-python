"""Generated from Smithy shape ``com.amazonaws.athena#StartSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.session_id
    import capo_athena.types.session_state


class StartSessionResponse(TypedDict, closed=True):
    session_id: NotRequired["capo_athena.types.session_id.SessionId"]
    """<p>The session ID.</p>"""
    state: NotRequired["capo_athena.types.session_state.SessionState"]
    """<p>The state of the session. A description of each state follows.</p> <p> <code>CREATING</code> - The session is being started, including acquiring resources.</p> <p> <code>CREATED</code> - The session has been started.</p> <p> <code>IDLE</code> - The session is able to accept a calculation.</p> <p> <code>BUSY</code> - The session is processing another task and is unable to accept a calculation.</p> <p> <code>TERMINATING</code> - The session is in the process of shutting down.</p> <p> <code>TERMINATED</code> - The session and its resources are no longer running.</p> <p> <code>DEGRADED</code> - The session has no healthy coordinators.</p> <p> <code>FAILED</code> - Due to a failure, the session and its resources are no longer running.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSessionResponse) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "state" in value:
        import capo_athena.types.session_state

        out["State"] = capo_athena.types.session_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSessionResponse:
    out: StartSessionResponse = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    if "State" in data:
        import capo_athena.types.session_state

        out["state"] = capo_athena.types.session_state.deserialize_aws_json_1_1(
            data["State"]
        )
    return out
