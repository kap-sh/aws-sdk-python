"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DeleteSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.session_identifier


class DeleteSessionRequest(TypedDict):
    session_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.session_identifier.SessionIdentifier"
    )
    """<p>The unique identifier for the session to be deleted. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSessionRequest:
    out: DeleteSessionRequest = {}  # type: ignore[typeddict-item]
    return out
