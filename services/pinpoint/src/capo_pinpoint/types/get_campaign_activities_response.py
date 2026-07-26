"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetCampaignActivitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.activities_response


class GetCampaignActivitiesResponse(TypedDict, closed=True):
    activities_response: NotRequired[
        "capo_pinpoint.types.activities_response.ActivitiesResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignActivitiesResponse) -> dict:
    out: dict = {}
    if "activities_response" in value:
        import capo_pinpoint.types.activities_response

        out["ActivitiesResponse"] = (
            capo_pinpoint.types.activities_response.serialize_json(
                value["activities_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCampaignActivitiesResponse:
    out: GetCampaignActivitiesResponse = {}  # type: ignore[typeddict-item]
    if "ActivitiesResponse" in data:
        import capo_pinpoint.types.activities_response

        out["activities_response"] = (
            capo_pinpoint.types.activities_response.deserialize_json(
                data["ActivitiesResponse"]
            )
        )
    return out
