"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListEventPredictionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.list_of_event_prediction_summaries
    import aws_sdk_frauddetector.types.string


class ListEventPredictionsResult(TypedDict):
    event_prediction_summaries: NotRequired[
        "aws_sdk_frauddetector.types.list_of_event_prediction_summaries.ListOfEventPredictionSummaries"
    ]
    """<p> The summary of the past predictions. </p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p> Identifies the next page of results to return. Use the token to make the call again to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventPredictionsResult) -> dict:
    out: dict = {}
    if "event_prediction_summaries" in value:
        import aws_sdk_frauddetector.types.list_of_event_prediction_summaries

        out["eventPredictionSummaries"] = (
            aws_sdk_frauddetector.types.list_of_event_prediction_summaries.serialize_aws_json_1_1(
                value["event_prediction_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventPredictionsResult:
    out: ListEventPredictionsResult = {}  # type: ignore[typeddict-item]
    if "eventPredictionSummaries" in data:
        import aws_sdk_frauddetector.types.list_of_event_prediction_summaries

        out["event_prediction_summaries"] = (
            aws_sdk_frauddetector.types.list_of_event_prediction_summaries.deserialize_aws_json_1_1(
                data["eventPredictionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
