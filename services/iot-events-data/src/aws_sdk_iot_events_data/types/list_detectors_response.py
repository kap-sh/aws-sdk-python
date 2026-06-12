"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#ListDetectorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.detector_summaries
    import aws_sdk_iot_events_data.types.next_token


class ListDetectorsResponse(TypedDict):
    detector_summaries: NotRequired[
        "aws_sdk_iot_events_data.types.detector_summaries.DetectorSummaries"
    ]
    """<p>A list of summary information about the detectors (instances).</p>"""
    next_token: NotRequired["aws_sdk_iot_events_data.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results, or <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectorsResponse) -> dict:
    out: dict = {}
    if "detector_summaries" in value:
        import aws_sdk_iot_events_data.types.detector_summaries

        out["detectorSummaries"] = (
            aws_sdk_iot_events_data.types.detector_summaries.serialize_json(
                value["detector_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDetectorsResponse:
    out: ListDetectorsResponse = {}  # type: ignore[typeddict-item]
    if "detectorSummaries" in data:
        import aws_sdk_iot_events_data.types.detector_summaries

        out["detector_summaries"] = (
            aws_sdk_iot_events_data.types.detector_summaries.deserialize_json(
                data["detectorSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
