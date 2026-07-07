"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetBrowserProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_id


class GetBrowserProfileRequest(TypedDict, closed=True):
    profile_id: (
        "aws_sdk_bedrock_agentcore_control.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the browser profile to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBrowserProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBrowserProfileRequest:
    out: GetBrowserProfileRequest = {}  # type: ignore[typeddict-item]
    return out
