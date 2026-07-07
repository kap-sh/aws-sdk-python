"""Generated from Smithy shape ``com.amazonaws.iotevents#ListDetectorModelVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.detector_model_version_summaries
    import aws_sdk_iot_events.types.next_token


class ListDetectorModelVersionsResponse(TypedDict, closed=True):
    detector_model_version_summaries: NotRequired[
        "aws_sdk_iot_events.types.detector_model_version_summaries.DetectorModelVersionSummaries"
    ]
    """<p>Summary information about the detector model versions.</p>"""
    next_token: NotRequired["aws_sdk_iot_events.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results, or <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectorModelVersionsResponse) -> dict:
    out: dict = {}
    if "detector_model_version_summaries" in value:
        import aws_sdk_iot_events.types.detector_model_version_summaries

        out["detectorModelVersionSummaries"] = (
            aws_sdk_iot_events.types.detector_model_version_summaries.serialize_json(
                value["detector_model_version_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDetectorModelVersionsResponse:
    out: ListDetectorModelVersionsResponse = {}  # type: ignore[typeddict-item]
    if "detectorModelVersionSummaries" in data:
        import aws_sdk_iot_events.types.detector_model_version_summaries

        out["detector_model_version_summaries"] = (
            aws_sdk_iot_events.types.detector_model_version_summaries.deserialize_json(
                data["detectorModelVersionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
