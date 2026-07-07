"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetUserJourneyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.user_journey


class GetUserJourneyResponse(TypedDict, closed=True):
    user_journey: "aws_sdk_resiliencehubv2.types.user_journey.UserJourney"
    """<p>The requested user journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserJourneyResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.user_journey

    out["userJourney"] = aws_sdk_resiliencehubv2.types.user_journey.serialize_json(
        value["user_journey"]
    )
    return out


def deserialize_json(data: dict) -> GetUserJourneyResponse:
    out: GetUserJourneyResponse = {}  # type: ignore[typeddict-item]
    if "userJourney" in data:
        import aws_sdk_resiliencehubv2.types.user_journey

        out["user_journey"] = (
            aws_sdk_resiliencehubv2.types.user_journey.deserialize_json(
                data["userJourney"]
            )
        )
    else:
        raise DeserializationError("GetUserJourneyResponse.user_journey required")
    return out
