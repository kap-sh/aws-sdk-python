"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetBrowserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_id


class GetBrowserRequest(TypedDict, closed=True):
    browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the browser to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBrowserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBrowserRequest:
    out: GetBrowserRequest = {}  # type: ignore[typeddict-item]
    return out
