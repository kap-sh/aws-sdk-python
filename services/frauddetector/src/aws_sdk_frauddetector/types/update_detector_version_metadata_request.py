"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateDetectorVersionMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.whole_number_version_string


class UpdateDetectorVersionMetadataRequest(TypedDict):
    detector_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The detector ID.</p>"""
    detector_version_id: "aws_sdk_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    """<p>The detector version ID. </p>"""
    description: "aws_sdk_frauddetector.types.description.description"
    """<p>The description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDetectorVersionMetadataRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    out["detectorVersionId"] = value["detector_version_id"]
    out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDetectorVersionMetadataRequest:
    out: UpdateDetectorVersionMetadataRequest = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError(
            "UpdateDetectorVersionMetadataRequest.detector_id required"
        )
    if "detectorVersionId" in data:
        out["detector_version_id"] = data["detectorVersionId"]
    else:
        raise DeserializationError(
            "UpdateDetectorVersionMetadataRequest.detector_version_id required"
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "UpdateDetectorVersionMetadataRequest.description required"
        )
    return out
