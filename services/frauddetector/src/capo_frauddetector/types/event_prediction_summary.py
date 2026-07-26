"""Generated from Smithy shape ``com.amazonaws.frauddetector#EventPredictionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.time
    import capo_frauddetector.types.whole_number_version_string


class EventPredictionSummary(TypedDict, closed=True):
    event_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p> The event ID. </p>"""
    event_type_name: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p> The event type. </p>"""
    event_timestamp: NotRequired["capo_frauddetector.types.time.time"]
    """<p> The timestamp of the event. </p>"""
    prediction_timestamp: NotRequired["capo_frauddetector.types.time.time"]
    """<p> The timestamp when the prediction was generated. </p>"""
    detector_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p> The detector ID. </p>"""
    detector_version_id: NotRequired[
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p> The detector version ID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventPredictionSummary) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "event_timestamp" in value:
        out["eventTimestamp"] = value["event_timestamp"]
    if "prediction_timestamp" in value:
        out["predictionTimestamp"] = value["prediction_timestamp"]
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "detector_version_id" in value:
        out["detectorVersionId"] = value["detector_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventPredictionSummary:
    out: EventPredictionSummary = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    if "eventTimestamp" in data:
        out["event_timestamp"] = data["eventTimestamp"]
    if "predictionTimestamp" in data:
        out["prediction_timestamp"] = data["predictionTimestamp"]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "detectorVersionId" in data:
        out["detector_version_id"] = data["detectorVersionId"]
    return out
