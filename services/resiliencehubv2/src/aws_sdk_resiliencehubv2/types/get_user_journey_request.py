"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetUserJourneyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.user_journey_id


class GetUserJourneyRequest(TypedDict):
    system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    user_journey_id: "aws_sdk_resiliencehubv2.types.user_journey_id.UserJourneyId"
    """<p>The identifier of the user journey to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserJourneyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUserJourneyRequest:
    out: GetUserJourneyRequest = {}  # type: ignore[typeddict-item]
    return out
