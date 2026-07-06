"""Generated from Smithy shape ``com.amazonaws.athena#SessionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.date
    import aws_sdk_athena.types.description_string
    import aws_sdk_athena.types.session_state


class SessionStatus(TypedDict, closed=True):
    start_date_time: NotRequired["aws_sdk_athena.types.date.Date"]
    """<p>The date and time that the session started.</p>"""
    last_modified_date_time: NotRequired["aws_sdk_athena.types.date.Date"]
    """<p>The most recent date and time that the session was modified.</p>"""
    end_date_time: NotRequired["aws_sdk_athena.types.date.Date"]
    """<p>The date and time that the session ended.</p>"""
    idle_since_date_time: NotRequired["aws_sdk_athena.types.date.Date"]
    """<p>The date and time starting at which the session became idle. Can be empty if the session is not currently idle.</p>"""
    state: NotRequired["aws_sdk_athena.types.session_state.SessionState"]
    """<p>The state of the session. A description of each state follows.</p> <p> <code>CREATING</code> - The session is being started, including acquiring resources.</p> <p> <code>CREATED</code> - The session has been started.</p> <p> <code>IDLE</code> - The session is able to accept a calculation.</p> <p> <code>BUSY</code> - The session is processing another task and is unable to accept a calculation.</p> <p> <code>TERMINATING</code> - The session is in the process of shutting down.</p> <p> <code>TERMINATED</code> - The session and its resources are no longer running.</p> <p> <code>DEGRADED</code> - The session has no healthy coordinators.</p> <p> <code>FAILED</code> - Due to a failure, the session and its resources are no longer running.</p>"""
    state_change_reason: NotRequired[
        "aws_sdk_athena.types.description_string.DescriptionString"
    ]
    """<p>The reason for the session state change (for example, canceled because the session was terminated).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionStatus) -> dict:
    out: dict = {}
    if "start_date_time" in value:
        import aws_sdk_athena.types.date

        out["StartDateTime"] = aws_sdk_athena.types.date.serialize_aws_json_1_1(
            value["start_date_time"]
        )
    if "last_modified_date_time" in value:
        import aws_sdk_athena.types.date

        out["LastModifiedDateTime"] = aws_sdk_athena.types.date.serialize_aws_json_1_1(
            value["last_modified_date_time"]
        )
    if "end_date_time" in value:
        import aws_sdk_athena.types.date

        out["EndDateTime"] = aws_sdk_athena.types.date.serialize_aws_json_1_1(
            value["end_date_time"]
        )
    if "idle_since_date_time" in value:
        import aws_sdk_athena.types.date

        out["IdleSinceDateTime"] = aws_sdk_athena.types.date.serialize_aws_json_1_1(
            value["idle_since_date_time"]
        )
    if "state" in value:
        import aws_sdk_athena.types.session_state

        out["State"] = aws_sdk_athena.types.session_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_change_reason" in value:
        out["StateChangeReason"] = value["state_change_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionStatus:
    out: SessionStatus = {}  # type: ignore[typeddict-item]
    if "StartDateTime" in data:
        import aws_sdk_athena.types.date

        out["start_date_time"] = aws_sdk_athena.types.date.deserialize_aws_json_1_1(
            data["StartDateTime"]
        )
    if "LastModifiedDateTime" in data:
        import aws_sdk_athena.types.date

        out["last_modified_date_time"] = (
            aws_sdk_athena.types.date.deserialize_aws_json_1_1(
                data["LastModifiedDateTime"]
            )
        )
    if "EndDateTime" in data:
        import aws_sdk_athena.types.date

        out["end_date_time"] = aws_sdk_athena.types.date.deserialize_aws_json_1_1(
            data["EndDateTime"]
        )
    if "IdleSinceDateTime" in data:
        import aws_sdk_athena.types.date

        out["idle_since_date_time"] = (
            aws_sdk_athena.types.date.deserialize_aws_json_1_1(
                data["IdleSinceDateTime"]
            )
        )
    if "State" in data:
        import aws_sdk_athena.types.session_state

        out["state"] = aws_sdk_athena.types.session_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateChangeReason" in data:
        out["state_change_reason"] = data["StateChangeReason"]
    return out
