"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StreamingConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class StreamingConfiguration(TypedDict, closed=True):
    enable_response_streaming: NotRequired["bool"]
    """<p>Indicates whether response streaming is enabled for the gateway. When set to <code>true</code>, the gateway streams responses from targets back to the client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamingConfiguration) -> dict:
    out: dict = {}
    if "enable_response_streaming" in value:
        out["enableResponseStreaming"] = value["enable_response_streaming"]
    return out


def deserialize_json(data: dict) -> StreamingConfiguration:
    out: StreamingConfiguration = {}  # type: ignore[typeddict-item]
    if "enableResponseStreaming" in data:
        out["enable_response_streaming"] = data["enableResponseStreaming"]
    return out
