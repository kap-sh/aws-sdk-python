"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UserJourney``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_label
    import capo_resiliencehubv2.types.user_journey_id


class UserJourney(TypedDict, closed=True):
    user_journey_id: "capo_resiliencehubv2.types.user_journey_id.UserJourneyId"
    """<p>The unique identifier of the user journey.</p>"""
    name: "capo_resiliencehubv2.types.entity_label.EntityLabel"
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the user journey was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the user journey was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserJourney) -> dict:
    out: dict = {}
    out["userJourneyId"] = value["user_journey_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> UserJourney:
    out: UserJourney = {}  # type: ignore[typeddict-item]
    if "userJourneyId" in data:
        out["user_journey_id"] = data["userJourneyId"]
    else:
        raise DeserializationError("UserJourney.user_journey_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UserJourney.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "createdAt" in data:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
