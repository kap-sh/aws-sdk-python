"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#UpdateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.session_identifier
    import aws_sdk_bedrock_agent_runtime.types.session_metadata_map


class UpdateSessionRequest(TypedDict, closed=True):
    session_metadata: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.session_metadata_map.SessionMetadataMap"
    ]
    """<p>A map of key-value pairs containing attributes to be persisted across the session. For example the user's ID, their language preference, and the type of device they are using.</p>"""
    session_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.session_identifier.SessionIdentifier"
    )
    """<p>The unique identifier of the session to modify. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionRequest) -> dict:
    out: dict = {}
    if "session_metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.session_metadata_map

        out["sessionMetadata"] = (
            aws_sdk_bedrock_agent_runtime.types.session_metadata_map.serialize_json(
                value["session_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSessionRequest:
    out: UpdateSessionRequest = {}  # type: ignore[typeddict-item]
    if "sessionMetadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.session_metadata_map

        out["session_metadata"] = (
            aws_sdk_bedrock_agent_runtime.types.session_metadata_map.deserialize_json(
                data["sessionMetadata"]
            )
        )
    return out
