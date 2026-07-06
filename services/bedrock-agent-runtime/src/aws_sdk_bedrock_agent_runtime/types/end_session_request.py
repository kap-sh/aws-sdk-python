"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#EndSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.session_identifier


class EndSessionRequest(TypedDict, closed=True):
    session_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.session_identifier.SessionIdentifier"
    )
    """<p>The unique identifier for the session to end. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EndSessionRequest:
    out: EndSessionRequest = {}  # type: ignore[typeddict-item]
    return out
