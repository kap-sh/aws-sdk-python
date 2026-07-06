"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.session_identifier


class GetSessionRequest(TypedDict, closed=True):
    session_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.session_identifier.SessionIdentifier"
    )
    """<p>A unique identifier for the session to retrieve. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionRequest:
    out: GetSessionRequest = {}  # type: ignore[typeddict-item]
    return out
