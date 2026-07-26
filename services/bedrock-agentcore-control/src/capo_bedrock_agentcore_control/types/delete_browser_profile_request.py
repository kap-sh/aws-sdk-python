"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteBrowserProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_profile_id
    import capo_bedrock_agentcore_control.types.client_token


class DeleteBrowserProfileRequest(TypedDict, closed=True):
    profile_id: (
        "capo_bedrock_agentcore_control.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the browser profile to delete.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrowserProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBrowserProfileRequest:
    out: DeleteBrowserProfileRequest = {}  # type: ignore[typeddict-item]
    return out
