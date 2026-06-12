"""Generated from Smithy shape ``com.amazonaws.athena#TerminateSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.session_state


class TerminateSessionResponse(TypedDict):
    state: NotRequired["aws_sdk_athena.types.session_state.SessionState"]
    """<p>The state of the session. A description of each state follows.</p> <p> <code>CREATING</code> - The session is being started, including acquiring resources.</p> <p> <code>CREATED</code> - The session has been started.</p> <p> <code>IDLE</code> - The session is able to accept a calculation.</p> <p> <code>BUSY</code> - The session is processing another task and is unable to accept a calculation.</p> <p> <code>TERMINATING</code> - The session is in the process of shutting down.</p> <p> <code>TERMINATED</code> - The session and its resources are no longer running.</p> <p> <code>DEGRADED</code> - The session has no healthy coordinators.</p> <p> <code>FAILED</code> - Due to a failure, the session and its resources are no longer running.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateSessionResponse) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_athena.types.session_state

        out["State"] = aws_sdk_athena.types.session_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateSessionResponse:
    out: TerminateSessionResponse = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_athena.types.session_state

        out["state"] = aws_sdk_athena.types.session_state.deserialize_aws_json_1_1(
            data["State"]
        )
    return out
