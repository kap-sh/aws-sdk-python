"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateDetectorVersionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.detector_version_status
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.whole_number_version_string


class UpdateDetectorVersionStatusRequest(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The detector ID. </p>"""
    detector_version_id: (
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    )
    """<p>The detector version ID. </p>"""
    status: "capo_frauddetector.types.detector_version_status.DetectorVersionStatus"
    """<p>The new status.</p> <p>The only supported values are <code>ACTIVE</code> and <code>INACTIVE</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDetectorVersionStatusRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    out["detectorVersionId"] = value["detector_version_id"]
    import capo_frauddetector.types.detector_version_status

    out["status"] = (
        capo_frauddetector.types.detector_version_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDetectorVersionStatusRequest:
    out: UpdateDetectorVersionStatusRequest = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError(
            "UpdateDetectorVersionStatusRequest.detector_id required"
        )
    if "detectorVersionId" in data:
        out["detector_version_id"] = data["detectorVersionId"]
    else:
        raise DeserializationError(
            "UpdateDetectorVersionStatusRequest.detector_version_id required"
        )
    if "status" in data:
        import capo_frauddetector.types.detector_version_status

        out["status"] = (
            capo_frauddetector.types.detector_version_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateDetectorVersionStatusRequest.status required")
    return out
