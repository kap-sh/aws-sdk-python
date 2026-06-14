"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StopRuntimeSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.http_response_code
    import aws_sdk_bedrock_agentcore.types.session_id


class StopRuntimeSessionResponse(TypedDict):
    runtime_session_id: NotRequired[
        "aws_sdk_bedrock_agentcore.types.session_id.SessionId"
    ]
    """<p>The ID of the session that you requested to stop.</p>"""
    status_code: NotRequired[
        "aws_sdk_bedrock_agentcore.types.http_response_code.HttpResponseCode"
    ]
    """<p>The status code of the request to stop the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopRuntimeSessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopRuntimeSessionResponse:
    out: StopRuntimeSessionResponse = {}  # type: ignore[typeddict-item]
    return out
