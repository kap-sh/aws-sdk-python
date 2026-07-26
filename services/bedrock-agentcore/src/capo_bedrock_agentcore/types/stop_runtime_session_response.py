"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StopRuntimeSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.http_response_code
    import capo_bedrock_agentcore.types.session_id


class StopRuntimeSessionResponse(TypedDict, closed=True):
    runtime_session_id: NotRequired["capo_bedrock_agentcore.types.session_id.SessionId"]
    """<p>The ID of the session that you requested to stop.</p>"""
    status_code: NotRequired[
        "capo_bedrock_agentcore.types.http_response_code.HttpResponseCode"
    ]
    """<p>The status code of the request to stop the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopRuntimeSessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopRuntimeSessionResponse:
    out: StopRuntimeSessionResponse = {}  # type: ignore[typeddict-item]
    return out
