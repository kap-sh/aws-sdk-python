"""Generated from Smithy shape ``com.amazonaws.iotevents#ListDetectorModelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.detector_model_summaries
    import aws_sdk_iot_events.types.next_token


class ListDetectorModelsResponse(TypedDict):
    detector_model_summaries: NotRequired[
        "aws_sdk_iot_events.types.detector_model_summaries.DetectorModelSummaries"
    ]
    """<p>Summary information about the detector models.</p>"""
    next_token: NotRequired["aws_sdk_iot_events.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results, or <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectorModelsResponse) -> dict:
    out: dict = {}
    if "detector_model_summaries" in value:
        import aws_sdk_iot_events.types.detector_model_summaries

        out["detectorModelSummaries"] = (
            aws_sdk_iot_events.types.detector_model_summaries.serialize_json(
                value["detector_model_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDetectorModelsResponse:
    out: ListDetectorModelsResponse = {}  # type: ignore[typeddict-item]
    if "detectorModelSummaries" in data:
        import aws_sdk_iot_events.types.detector_model_summaries

        out["detector_model_summaries"] = (
            aws_sdk_iot_events.types.detector_model_summaries.deserialize_json(
                data["detectorModelSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
