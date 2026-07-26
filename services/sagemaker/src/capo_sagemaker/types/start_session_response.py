"""Generated from Smithy shape ``com.amazonaws.sagemaker#StartSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.session_id
    import capo_sagemaker.types.stream_url
    import capo_sagemaker.types.token_value


class StartSessionResponse(TypedDict, closed=True):
    session_id: NotRequired["capo_sagemaker.types.session_id.SessionId"]
    """<p>A unique identifier for the established remote connection session.</p>"""
    stream_url: NotRequired["capo_sagemaker.types.stream_url.StreamUrl"]
    """<p>A WebSocket URL used to establish a SSH connection between the local IDE and remote SageMaker space.</p>"""
    token_value: NotRequired["capo_sagemaker.types.token_value.TokenValue"]
    """<p>An encrypted token value containing session and caller information. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSessionResponse) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "stream_url" in value:
        out["StreamUrl"] = value["stream_url"]
    if "token_value" in value:
        out["TokenValue"] = value["token_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSessionResponse:
    out: StartSessionResponse = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    if "StreamUrl" in data:
        out["stream_url"] = data["StreamUrl"]
    if "TokenValue" in data:
        out["token_value"] = data["TokenValue"]
    return out
