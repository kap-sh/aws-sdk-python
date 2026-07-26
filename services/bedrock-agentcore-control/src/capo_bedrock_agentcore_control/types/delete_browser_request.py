"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteBrowserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_id
    import capo_bedrock_agentcore_control.types.client_token


class DeleteBrowserRequest(TypedDict, closed=True):
    browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the browser to delete.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrowserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBrowserRequest:
    out: DeleteBrowserRequest = {}  # type: ignore[typeddict-item]
    return out
