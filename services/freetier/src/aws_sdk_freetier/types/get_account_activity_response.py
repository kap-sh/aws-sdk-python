"""Generated from Smithy shape ``com.amazonaws.freetier#GetAccountActivityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_freetier.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_freetier.types.activity_id
    import aws_sdk_freetier.types.activity_reward
    import aws_sdk_freetier.types.activity_status
    import aws_sdk_freetier.types.generic_string


class GetAccountActivityResponse(TypedDict):
    activity_id: "aws_sdk_freetier.types.activity_id.ActivityId"
    """<p> A unique identifier that identifies the activity. </p>"""
    title: "aws_sdk_freetier.types.generic_string.GenericString"
    """<p> A short activity title. </p>"""
    description: "aws_sdk_freetier.types.generic_string.GenericString"
    """<p> Provides detailed information about the activity and its expected outcomes. </p>"""
    status: "aws_sdk_freetier.types.activity_status.ActivityStatus"
    """<p> The current activity status. </p>"""
    instructions_url: "aws_sdk_freetier.types.generic_string.GenericString"
    """<p> The URL resource that provides guidance on activity requirements and completion. </p>"""
    reward: "aws_sdk_freetier.types.activity_reward.ActivityReward"
    """<p> A reward granted upon activity completion. </p>"""
    estimated_time_to_complete_in_minutes: NotRequired["int"]
    """<p> The estimated time to complete the activity. This is the duration in minutes. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The time by which the activity must be completed to receive a reward. </p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the activity started. This field appears only for activities in the <code>IN_PROGRESS</code> or <code>COMPLETED</code> states. </p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the activity is completed. This field appears only for activities in the <code>COMPLETED</code> state. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountActivityResponse) -> dict:
    out: dict = {}
    out["activityId"] = value["activity_id"]
    out["title"] = value["title"]
    out["description"] = value["description"]
    import aws_sdk_freetier.types.activity_status

    out["status"] = aws_sdk_freetier.types.activity_status.serialize_aws_json_1_0(
        value["status"]
    )
    out["instructionsUrl"] = value["instructions_url"]
    import aws_sdk_freetier.types.activity_reward

    out["reward"] = aws_sdk_freetier.types.activity_reward.serialize_aws_json_1_0(
        value["reward"]
    )
    if "estimated_time_to_complete_in_minutes" in value:
        out["estimatedTimeToCompleteInMinutes"] = value[
            "estimated_time_to_complete_in_minutes"
        ]
    if "expires_at" in value:
        import aws_sdk_freetier.types._prelude.timestamp

        out["expiresAt"] = (
            aws_sdk_freetier.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    if "started_at" in value:
        import aws_sdk_freetier.types._prelude.timestamp

        out["startedAt"] = (
            aws_sdk_freetier.types._prelude.timestamp.serialize_aws_json_1_0(
                value["started_at"]
            )
        )
    if "completed_at" in value:
        import aws_sdk_freetier.types._prelude.timestamp

        out["completedAt"] = (
            aws_sdk_freetier.types._prelude.timestamp.serialize_aws_json_1_0(
                value["completed_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountActivityResponse:
    out: GetAccountActivityResponse = {}  # type: ignore[typeddict-item]
    if "activityId" in data:
        out["activity_id"] = data["activityId"]
    else:
        raise DeserializationError("GetAccountActivityResponse.activity_id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("GetAccountActivityResponse.title required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("GetAccountActivityResponse.description required")
    if "status" in data:
        import aws_sdk_freetier.types.activity_status

        out["status"] = aws_sdk_freetier.types.activity_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("GetAccountActivityResponse.status required")
    if "instructionsUrl" in data:
        out["instructions_url"] = data["instructionsUrl"]
    else:
        raise DeserializationError(
            "GetAccountActivityResponse.instructions_url required"
        )
    if "reward" in data:
        import aws_sdk_freetier.types.activity_reward

        out["reward"] = aws_sdk_freetier.types.activity_reward.deserialize_aws_json_1_0(
            data["reward"]
        )
    else:
        raise DeserializationError("GetAccountActivityResponse.reward required")
    if "estimatedTimeToCompleteInMinutes" in data:
        out["estimated_time_to_complete_in_minutes"] = data[
            "estimatedTimeToCompleteInMinutes"
        ]
    if "expiresAt" in data:
        import aws_sdk_freetier.types._prelude.timestamp

        out["expires_at"] = (
            aws_sdk_freetier.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["expiresAt"]
            )
        )
    if "startedAt" in data:
        import aws_sdk_freetier.types._prelude.timestamp

        out["started_at"] = (
            aws_sdk_freetier.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startedAt"]
            )
        )
    if "completedAt" in data:
        import aws_sdk_freetier.types._prelude.timestamp

        out["completed_at"] = (
            aws_sdk_freetier.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["completedAt"]
            )
        )
    return out
