"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateUserJourneyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.user_journey


class UpdateUserJourneyResponse(TypedDict, closed=True):
    user_journey: "capo_resiliencehubv2.types.user_journey.UserJourney"
    """<p>The updated user journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserJourneyResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.user_journey

    out["userJourney"] = capo_resiliencehubv2.types.user_journey.serialize_json(
        value["user_journey"]
    )
    return out


def deserialize_json(data: dict) -> UpdateUserJourneyResponse:
    out: UpdateUserJourneyResponse = {}  # type: ignore[typeddict-item]
    if "userJourney" in data:
        import capo_resiliencehubv2.types.user_journey

        out["user_journey"] = capo_resiliencehubv2.types.user_journey.deserialize_json(
            data["userJourney"]
        )
    else:
        raise DeserializationError("UpdateUserJourneyResponse.user_journey required")
    return out
