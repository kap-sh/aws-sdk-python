"""Generated from Smithy shape ``com.amazonaws.ecs#Session``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.sensitive_string
    import capo_ecs.types.string


class Session(TypedDict, closed=True):
    session_id: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of the execute command session.</p>"""
    stream_url: NotRequired["capo_ecs.types.string.String"]
    """<p>A URL to the managed agent on the container that the SSM Session Manager client uses to send commands and receive output from the container.</p>"""
    token_value: NotRequired["capo_ecs.types.sensitive_string.SensitiveString"]
    """<p>An encrypted token value containing session and caller information. It's used to authenticate the connection to the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Session) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "stream_url" in value:
        out["streamUrl"] = value["stream_url"]
    if "token_value" in value:
        out["tokenValue"] = value["token_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "streamUrl" in data:
        out["stream_url"] = data["streamUrl"]
    if "tokenValue" in data:
        out["token_value"] = data["tokenValue"]
    return out
