"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LiveViewStream``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_stream_endpoint


class LiveViewStream(TypedDict, closed=True):
    stream_endpoint: NotRequired[
        "capo_bedrock_agentcore.types.browser_stream_endpoint.BrowserStreamEndpoint"
    ]
    """<p>The endpoint URL for the live view stream. This URL is used to establish a connection to receive visual updates from the browser session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LiveViewStream) -> dict:
    out: dict = {}
    if "stream_endpoint" in value:
        out["streamEndpoint"] = value["stream_endpoint"]
    return out


def deserialize_json(data: dict) -> LiveViewStream:
    out: LiveViewStream = {}  # type: ignore[typeddict-item]
    if data.get("streamEndpoint") is not None:
        out["stream_endpoint"] = data["streamEndpoint"]
    return out
