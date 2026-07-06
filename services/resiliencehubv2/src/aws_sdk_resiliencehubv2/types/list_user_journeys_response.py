"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListUserJourneysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.user_journey_summary_list


class ListUserJourneysResponse(TypedDict, closed=True):
    user_journey_summaries: (
        "aws_sdk_resiliencehubv2.types.user_journey_summary_list.UserJourneySummaryList"
    )
    """<p>The list of user journey summaries.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListUserJourneysResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.user_journey_summary_list

    out["userJourneySummaries"] = (
        aws_sdk_resiliencehubv2.types.user_journey_summary_list.serialize_json(
            value["user_journey_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUserJourneysResponse:
    out: ListUserJourneysResponse = {}  # type: ignore[typeddict-item]
    if "userJourneySummaries" in data:
        import aws_sdk_resiliencehubv2.types.user_journey_summary_list

        out["user_journey_summaries"] = (
            aws_sdk_resiliencehubv2.types.user_journey_summary_list.deserialize_json(
                data["userJourneySummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListUserJourneysResponse.user_journey_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
