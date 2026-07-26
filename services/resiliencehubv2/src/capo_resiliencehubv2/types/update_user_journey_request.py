"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateUserJourneyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_label
    import capo_resiliencehubv2.types.user_journey_id


class UpdateUserJourneyRequest(TypedDict, closed=True):
    system_arn: "capo_resiliencehubv2.types.arn.Arn"
    user_journey_id: "capo_resiliencehubv2.types.user_journey_id.UserJourneyId"
    """<p>The identifier of the user journey to update.</p>"""
    name: NotRequired["capo_resiliencehubv2.types.entity_label.EntityLabel"]
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserJourneyRequest) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    out["userJourneyId"] = value["user_journey_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> UpdateUserJourneyRequest:
    out: UpdateUserJourneyRequest = {}  # type: ignore[typeddict-item]
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    else:
        raise DeserializationError("UpdateUserJourneyRequest.system_arn required")
    if "userJourneyId" in data:
        out["user_journey_id"] = data["userJourneyId"]
    else:
        raise DeserializationError("UpdateUserJourneyRequest.user_journey_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    return out
