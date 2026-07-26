"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetDetectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.detectors_max_results
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.string


class GetDetectorsRequest(TypedDict, closed=True):
    detector_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The detector ID.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next token for the subsequent request.</p>"""
    max_results: NotRequired[
        "capo_frauddetector.types.detectors_max_results.DetectorsMaxResults"
    ]
    """<p>The maximum number of objects to return for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDetectorsRequest) -> dict:
    out: dict = {}
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDetectorsRequest:
    out: GetDetectorsRequest = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
