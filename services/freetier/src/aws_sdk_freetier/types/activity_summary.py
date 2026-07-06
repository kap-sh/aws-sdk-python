"""Generated from Smithy shape ``com.amazonaws.freetier#ActivitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_freetier.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_freetier.types.activity_id
    import aws_sdk_freetier.types.activity_reward
    import aws_sdk_freetier.types.activity_status
    import aws_sdk_freetier.types.generic_string


class ActivitySummary(TypedDict, closed=True):
    activity_id: "aws_sdk_freetier.types.activity_id.ActivityId"
    """<p> A unique identifier that identifies the activity. </p>"""
    title: "aws_sdk_freetier.types.generic_string.GenericString"
    """<p> The title of the activity. </p>"""
    reward: "aws_sdk_freetier.types.activity_reward.ActivityReward"
    """<p> The reward for the activity. </p>"""
    status: "aws_sdk_freetier.types.activity_status.ActivityStatus"
    """<p> The current status of the activity. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivitySummary) -> dict:
    out: dict = {}
    out["activityId"] = value["activity_id"]
    out["title"] = value["title"]
    import aws_sdk_freetier.types.activity_reward

    out["reward"] = aws_sdk_freetier.types.activity_reward.serialize_aws_json_1_0(
        value["reward"]
    )
    import aws_sdk_freetier.types.activity_status

    out["status"] = aws_sdk_freetier.types.activity_status.serialize_aws_json_1_0(
        value["status"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivitySummary:
    out: ActivitySummary = {}  # type: ignore[typeddict-item]
    if "activityId" in data:
        out["activity_id"] = data["activityId"]
    else:
        raise DeserializationError("ActivitySummary.activity_id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("ActivitySummary.title required")
    if "reward" in data:
        import aws_sdk_freetier.types.activity_reward

        out["reward"] = aws_sdk_freetier.types.activity_reward.deserialize_aws_json_1_0(
            data["reward"]
        )
    else:
        raise DeserializationError("ActivitySummary.reward required")
    if "status" in data:
        import aws_sdk_freetier.types.activity_status

        out["status"] = aws_sdk_freetier.types.activity_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("ActivitySummary.status required")
    return out
