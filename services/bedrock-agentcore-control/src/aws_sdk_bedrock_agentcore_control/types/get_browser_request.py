"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetBrowserRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_id


class GetBrowserRequest(TypedDict):
    browser_id: "aws_sdk_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the browser to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBrowserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBrowserRequest:
    out: GetBrowserRequest = {}  # type: ignore[typeddict-item]
    return out
