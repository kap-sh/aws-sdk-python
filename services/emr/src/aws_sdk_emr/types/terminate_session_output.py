"""Generated from Smithy shape ``com.amazonaws.emr#TerminateSessionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.session_id
    import aws_sdk_emr.types.session_state


class TerminateSessionOutput(TypedDict):
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>The ID of the cluster that the session belonged to.</p>"""
    session_id: NotRequired["aws_sdk_emr.types.session_id.SessionId"]
    """<p>The ID of the terminated session.</p>"""
    state: NotRequired["aws_sdk_emr.types.session_state.SessionState"]
    """<p>The state of the session after the terminate request has been accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateSessionOutput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "state" in value:
        import aws_sdk_emr.types.session_state

        out["State"] = aws_sdk_emr.types.session_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateSessionOutput:
    out: TerminateSessionOutput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    if "State" in data:
        import aws_sdk_emr.types.session_state

        out["state"] = aws_sdk_emr.types.session_state.deserialize_aws_json_1_1(
            data["State"]
        )
    return out
