"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetDetectorVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.whole_number_version_string


class GetDetectorVersionRequest(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The detector ID.</p>"""
    detector_version_id: (
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    )
    """<p>The detector version ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDetectorVersionRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    out["detectorVersionId"] = value["detector_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDetectorVersionRequest:
    out: GetDetectorVersionRequest = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError("GetDetectorVersionRequest.detector_id required")
    if "detectorVersionId" in data:
        out["detector_version_id"] = data["detectorVersionId"]
    else:
        raise DeserializationError(
            "GetDetectorVersionRequest.detector_version_id required"
        )
    return out
