"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteDetectorVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.whole_number_version_string


class DeleteDetectorVersionRequest(TypedDict, closed=True):
    detector_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The ID of the parent detector for the detector version to delete.</p>"""
    detector_version_id: "aws_sdk_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    """<p>The ID of the detector version to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDetectorVersionRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    out["detectorVersionId"] = value["detector_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDetectorVersionRequest:
    out: DeleteDetectorVersionRequest = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError("DeleteDetectorVersionRequest.detector_id required")
    if "detectorVersionId" in data:
        out["detector_version_id"] = data["detectorVersionId"]
    else:
        raise DeserializationError(
            "DeleteDetectorVersionRequest.detector_version_id required"
        )
    return out
