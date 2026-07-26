"""Generated from Smithy shape ``com.amazonaws.freetier#ActivitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_freetier.errors import DeserializationError

if TYPE_CHECKING:
    import capo_freetier.types.activity_id
    import capo_freetier.types.activity_reward
    import capo_freetier.types.activity_status
    import capo_freetier.types.generic_string


class ActivitySummary(TypedDict, closed=True):
    activity_id: "capo_freetier.types.activity_id.ActivityId"
    """<p> A unique identifier that identifies the activity. </p>"""
    title: "capo_freetier.types.generic_string.GenericString"
    """<p> The title of the activity. </p>"""
    reward: "capo_freetier.types.activity_reward.ActivityReward"
    """<p> The reward for the activity. </p>"""
    status: "capo_freetier.types.activity_status.ActivityStatus"
    """<p> The current status of the activity. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivitySummary) -> dict:
    out: dict = {}
    out["activityId"] = value["activity_id"]
    out["title"] = value["title"]
    import capo_freetier.types.activity_reward

    out["reward"] = capo_freetier.types.activity_reward.serialize_aws_json_1_0(
        value["reward"]
    )
    import capo_freetier.types.activity_status

    out["status"] = capo_freetier.types.activity_status.serialize_aws_json_1_0(
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
        import capo_freetier.types.activity_reward

        out["reward"] = capo_freetier.types.activity_reward.deserialize_aws_json_1_0(
            data["reward"]
        )
    else:
        raise DeserializationError("ActivitySummary.reward required")
    if "status" in data:
        import capo_freetier.types.activity_status

        out["status"] = capo_freetier.types.activity_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("ActivitySummary.status required")
    return out
