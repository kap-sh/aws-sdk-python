"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteUserJourneyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.user_journey_id


class DeleteUserJourneyRequest(TypedDict):
    system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    user_journey_id: "aws_sdk_resiliencehubv2.types.user_journey_id.UserJourneyId"
    """<p>The identifier of the user journey to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserJourneyRequest) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    out["userJourneyId"] = value["user_journey_id"]
    return out


def deserialize_json(data: dict) -> DeleteUserJourneyRequest:
    out: DeleteUserJourneyRequest = {}  # type: ignore[typeddict-item]
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    else:
        raise DeserializationError("DeleteUserJourneyRequest.system_arn required")
    if "userJourneyId" in data:
        out["user_journey_id"] = data["userJourneyId"]
    else:
        raise DeserializationError("DeleteUserJourneyRequest.user_journey_id required")
    return out
