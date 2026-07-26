"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateBrowserProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_profile_arn
    import capo_bedrock_agentcore_control.types.browser_profile_id
    import capo_bedrock_agentcore_control.types.browser_profile_status
    import capo_bedrock_agentcore_control.types.date_timestamp


class CreateBrowserProfileResponse(TypedDict, closed=True):
    profile_id: (
        "capo_bedrock_agentcore_control.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the created browser profile.</p>"""
    profile_arn: (
        "capo_bedrock_agentcore_control.types.browser_profile_arn.BrowserProfileArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created browser profile.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser profile was created.</p>"""
    status: "capo_bedrock_agentcore_control.types.browser_profile_status.BrowserProfileStatus"
    """<p>The current status of the browser profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrowserProfileResponse) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["profileArn"] = value["profile_arn"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.browser_profile_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.browser_profile_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateBrowserProfileResponse:
    out: CreateBrowserProfileResponse = {}  # type: ignore[typeddict-item]
    if "profileId" in data:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("CreateBrowserProfileResponse.profile_id required")
    if "profileArn" in data:
        out["profile_arn"] = data["profileArn"]
    else:
        raise DeserializationError("CreateBrowserProfileResponse.profile_arn required")
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateBrowserProfileResponse.created_at required")
    if "status" in data:
        import capo_bedrock_agentcore_control.types.browser_profile_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.browser_profile_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateBrowserProfileResponse.status required")
    return out
