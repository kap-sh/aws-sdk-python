"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SaveBrowserSessionProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_profile_id
    import aws_sdk_bedrock_agentcore.types.browser_session_id
    import aws_sdk_bedrock_agentcore.types.date_timestamp


class SaveBrowserSessionProfileResponse(TypedDict, closed=True):
    profile_identifier: (
        "aws_sdk_bedrock_agentcore.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the saved browser profile.</p>"""
    browser_identifier: "str"
    """<p>The unique identifier of the browser associated with the session from which the profile was saved.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The unique identifier of the browser session from which the profile was saved.</p>"""
    last_updated_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser profile was last updated. This value is in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaveBrowserSessionProfileResponse) -> dict:
    out: dict = {}
    out["profileIdentifier"] = value["profile_identifier"]
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["lastUpdatedAt"] = (
        aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> SaveBrowserSessionProfileResponse:
    out: SaveBrowserSessionProfileResponse = {}  # type: ignore[typeddict-item]
    if "profileIdentifier" in data:
        out["profile_identifier"] = data["profileIdentifier"]
    else:
        raise DeserializationError(
            "SaveBrowserSessionProfileResponse.profile_identifier required"
        )
    if "browserIdentifier" in data:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        raise DeserializationError(
            "SaveBrowserSessionProfileResponse.browser_identifier required"
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError(
            "SaveBrowserSessionProfileResponse.session_id required"
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "SaveBrowserSessionProfileResponse.last_updated_at required"
        )
    return out
