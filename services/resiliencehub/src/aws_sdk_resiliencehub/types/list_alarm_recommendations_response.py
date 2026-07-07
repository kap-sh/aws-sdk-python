"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAlarmRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.alarm_recommendation_list
    import aws_sdk_resiliencehub.types.next_token


class ListAlarmRecommendationsResponse(TypedDict, closed=True):
    alarm_recommendations: (
        "aws_sdk_resiliencehub.types.alarm_recommendation_list.AlarmRecommendationList"
    )
    """<p>The alarm recommendations for an Resilience Hub application, returned as an object. This object includes Application Component names, descriptions, information about whether a recommendation has already been implemented or not, prerequisites, and more.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAlarmRecommendationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.alarm_recommendation_list

    out["alarmRecommendations"] = (
        aws_sdk_resiliencehub.types.alarm_recommendation_list.serialize_json(
            value["alarm_recommendations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAlarmRecommendationsResponse:
    out: ListAlarmRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "alarmRecommendations" in data:
        import aws_sdk_resiliencehub.types.alarm_recommendation_list

        out["alarm_recommendations"] = (
            aws_sdk_resiliencehub.types.alarm_recommendation_list.deserialize_json(
                data["alarmRecommendations"]
            )
        )
    else:
        raise DeserializationError(
            "ListAlarmRecommendationsResponse.alarm_recommendations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
