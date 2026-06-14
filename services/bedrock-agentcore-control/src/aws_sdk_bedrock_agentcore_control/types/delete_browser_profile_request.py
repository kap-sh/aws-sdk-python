"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteBrowserProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_id
    import aws_sdk_bedrock_agentcore_control.types.client_token


class DeleteBrowserProfileRequest(TypedDict):
    profile_id: (
        "aws_sdk_bedrock_agentcore_control.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the browser profile to delete.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrowserProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBrowserProfileRequest:
    out: DeleteBrowserProfileRequest = {}  # type: ignore[typeddict-item]
    return out
