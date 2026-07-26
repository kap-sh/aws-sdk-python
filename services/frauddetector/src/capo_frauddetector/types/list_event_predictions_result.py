"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListEventPredictionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.list_of_event_prediction_summaries
    import capo_frauddetector.types.string


class ListEventPredictionsResult(TypedDict, closed=True):
    event_prediction_summaries: NotRequired[
        "capo_frauddetector.types.list_of_event_prediction_summaries.ListOfEventPredictionSummaries"
    ]
    """<p> The summary of the past predictions. </p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p> Identifies the next page of results to return. Use the token to make the call again to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventPredictionsResult) -> dict:
    out: dict = {}
    if "event_prediction_summaries" in value:
        import capo_frauddetector.types.list_of_event_prediction_summaries

        out["eventPredictionSummaries"] = (
            capo_frauddetector.types.list_of_event_prediction_summaries.serialize_aws_json_1_1(
                value["event_prediction_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventPredictionsResult:
    out: ListEventPredictionsResult = {}  # type: ignore[typeddict-item]
    if "eventPredictionSummaries" in data:
        import capo_frauddetector.types.list_of_event_prediction_summaries

        out["event_prediction_summaries"] = (
            capo_frauddetector.types.list_of_event_prediction_summaries.deserialize_aws_json_1_1(
                data["eventPredictionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
