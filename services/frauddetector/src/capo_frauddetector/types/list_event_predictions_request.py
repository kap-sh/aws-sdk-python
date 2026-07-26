"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListEventPredictionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.event_predictions_max_results
    import capo_frauddetector.types.filter_condition
    import capo_frauddetector.types.prediction_time_range
    import capo_frauddetector.types.string


class ListEventPredictionsRequest(TypedDict, closed=True):
    event_id: NotRequired["capo_frauddetector.types.filter_condition.FilterCondition"]
    """<p> The event ID. </p>"""
    event_type: NotRequired["capo_frauddetector.types.filter_condition.FilterCondition"]
    """<p> The event type associated with the detector. </p>"""
    detector_id: NotRequired[
        "capo_frauddetector.types.filter_condition.FilterCondition"
    ]
    """<p> The detector ID. </p>"""
    detector_version_id: NotRequired[
        "capo_frauddetector.types.filter_condition.FilterCondition"
    ]
    """<p> The detector version ID. </p>"""
    prediction_time_range: NotRequired[
        "capo_frauddetector.types.prediction_time_range.PredictionTimeRange"
    ]
    """<p> The time period for when the predictions were generated. </p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p> Identifies the next page of results to return. Use the token to make the call again to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""
    max_results: NotRequired[
        "capo_frauddetector.types.event_predictions_max_results.EventPredictionsMaxResults"
    ]
    """<p> The maximum number of predictions to return for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventPredictionsRequest) -> dict:
    out: dict = {}
    if "event_id" in value:
        import capo_frauddetector.types.filter_condition

        out["eventId"] = (
            capo_frauddetector.types.filter_condition.serialize_aws_json_1_1(
                value["event_id"]
            )
        )
    if "event_type" in value:
        import capo_frauddetector.types.filter_condition

        out["eventType"] = (
            capo_frauddetector.types.filter_condition.serialize_aws_json_1_1(
                value["event_type"]
            )
        )
    if "detector_id" in value:
        import capo_frauddetector.types.filter_condition

        out["detectorId"] = (
            capo_frauddetector.types.filter_condition.serialize_aws_json_1_1(
                value["detector_id"]
            )
        )
    if "detector_version_id" in value:
        import capo_frauddetector.types.filter_condition

        out["detectorVersionId"] = (
            capo_frauddetector.types.filter_condition.serialize_aws_json_1_1(
                value["detector_version_id"]
            )
        )
    if "prediction_time_range" in value:
        import capo_frauddetector.types.prediction_time_range

        out["predictionTimeRange"] = (
            capo_frauddetector.types.prediction_time_range.serialize_aws_json_1_1(
                value["prediction_time_range"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventPredictionsRequest:
    out: ListEventPredictionsRequest = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        import capo_frauddetector.types.filter_condition

        out["event_id"] = (
            capo_frauddetector.types.filter_condition.deserialize_aws_json_1_1(
                data["eventId"]
            )
        )
    if "eventType" in data:
        import capo_frauddetector.types.filter_condition

        out["event_type"] = (
            capo_frauddetector.types.filter_condition.deserialize_aws_json_1_1(
                data["eventType"]
            )
        )
    if "detectorId" in data:
        import capo_frauddetector.types.filter_condition

        out["detector_id"] = (
            capo_frauddetector.types.filter_condition.deserialize_aws_json_1_1(
                data["detectorId"]
            )
        )
    if "detectorVersionId" in data:
        import capo_frauddetector.types.filter_condition

        out["detector_version_id"] = (
            capo_frauddetector.types.filter_condition.deserialize_aws_json_1_1(
                data["detectorVersionId"]
            )
        )
    if "predictionTimeRange" in data:
        import capo_frauddetector.types.prediction_time_range

        out["prediction_time_range"] = (
            capo_frauddetector.types.prediction_time_range.deserialize_aws_json_1_1(
                data["predictionTimeRange"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
