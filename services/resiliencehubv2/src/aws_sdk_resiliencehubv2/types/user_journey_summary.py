"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UserJourneySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.entity_label
    import aws_sdk_resiliencehubv2.types.user_journey_id


class UserJourneySummary(TypedDict, closed=True):
    user_journey_id: "aws_sdk_resiliencehubv2.types.user_journey_id.UserJourneyId"
    """<p>The unique identifier of the user journey.</p>"""
    name: "aws_sdk_resiliencehubv2.types.entity_label.EntityLabel"
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the user journey was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the user journey was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserJourneySummary) -> dict:
    out: dict = {}
    out["userJourneyId"] = value["user_journey_id"]
    out["name"] = value["name"]
    if "created_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserJourneySummary:
    out: UserJourneySummary = {}  # type: ignore[typeddict-item]
    if "userJourneyId" in data:
        out["user_journey_id"] = data["userJourneyId"]
    else:
        raise DeserializationError("UserJourneySummary.user_journey_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UserJourneySummary.name required")
    if "createdAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
