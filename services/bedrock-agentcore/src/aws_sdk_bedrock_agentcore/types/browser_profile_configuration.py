"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserProfileConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_profile_id

class BrowserProfileConfiguration(TypedDict):
    profile_identifier: "aws_sdk_bedrock_agentcore.types.browser_profile_id.BrowserProfileId"
    """<p>The unique identifier of the browser profile. This identifier is used to reference the profile when starting new browser sessions or saving session data to the profile.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BrowserProfileConfiguration) -> dict:
    out: dict = {}
    out["profileIdentifier"] = value["profile_identifier"]
    return out


def deserialize_json(data: dict) -> BrowserProfileConfiguration:
    out: BrowserProfileConfiguration = {}  # type: ignore[typeddict-item]
    if "profileIdentifier" in data:
        out["profile_identifier"] = data["profileIdentifier"]
    else:
        raise DeserializationError("BrowserProfileConfiguration.profile_identifier required")
    return out