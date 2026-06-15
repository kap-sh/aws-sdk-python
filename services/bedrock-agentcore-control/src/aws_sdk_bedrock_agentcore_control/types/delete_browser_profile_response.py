"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteBrowserProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_arn
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_id
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_status
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp


class DeleteBrowserProfileResponse(TypedDict):
    profile_id: (
        "aws_sdk_bedrock_agentcore_control.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the deleted browser profile.</p>"""
    profile_arn: (
        "aws_sdk_bedrock_agentcore_control.types.browser_profile_arn.BrowserProfileArn"
    )
    """<p>The Amazon Resource Name (ARN) of the deleted browser profile.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.browser_profile_status.BrowserProfileStatus"
    """<p>The current status of the browser profile deletion.</p>"""
    last_updated_at: (
        "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp when the browser profile was last updated.</p>"""
    last_saved_at: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when browser session data was last saved to this profile before deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrowserProfileResponse) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["profileArn"] = value["profile_arn"]
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.browser_profile_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    if "last_saved_at" in value:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["lastSavedAt"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
                value["last_saved_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteBrowserProfileResponse:
    out: DeleteBrowserProfileResponse = {}  # type: ignore[typeddict-item]
    if "profileId" in data:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("DeleteBrowserProfileResponse.profile_id required")
    if "profileArn" in data:
        out["profile_arn"] = data["profileArn"]
    else:
        raise DeserializationError("DeleteBrowserProfileResponse.profile_arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_profile_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.browser_profile_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteBrowserProfileResponse.status required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteBrowserProfileResponse.last_updated_at required"
        )
    if "lastSavedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["last_saved_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastSavedAt"]
            )
        )
    return out
