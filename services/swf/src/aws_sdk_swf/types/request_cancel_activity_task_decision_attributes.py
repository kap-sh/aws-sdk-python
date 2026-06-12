"""Generated from Smithy shape ``com.amazonaws.swf#RequestCancelActivityTaskDecisionAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.activity_id


class RequestCancelActivityTaskDecisionAttributes(TypedDict):
    activity_id: "aws_sdk_swf.types.activity_id.ActivityId"
    """<p>The <code>activityId</code> of the activity task to be canceled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestCancelActivityTaskDecisionAttributes) -> dict:
    out: dict = {}
    out["activityId"] = value["activity_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestCancelActivityTaskDecisionAttributes:
    out: RequestCancelActivityTaskDecisionAttributes = {}  # type: ignore[typeddict-item]
    if "activityId" in data:
        out["activity_id"] = data["activityId"]
    else:
        raise DeserializationError(
            "RequestCancelActivityTaskDecisionAttributes.activity_id required"
        )
    return out
