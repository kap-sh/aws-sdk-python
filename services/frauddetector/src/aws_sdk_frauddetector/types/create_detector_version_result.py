"""Generated from Smithy shape ``com.amazonaws.frauddetector#CreateDetectorVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.detector_version_status
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.whole_number_version_string


class CreateDetectorVersionResult(TypedDict, closed=True):
    detector_id: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The ID for the created version's parent detector.</p>"""
    detector_version_id: NotRequired[
        "aws_sdk_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p>The ID for the created detector. </p>"""
    status: NotRequired[
        "aws_sdk_frauddetector.types.detector_version_status.DetectorVersionStatus"
    ]
    """<p>The status of the detector version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDetectorVersionResult) -> dict:
    out: dict = {}
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "detector_version_id" in value:
        out["detectorVersionId"] = value["detector_version_id"]
    if "status" in value:
        import aws_sdk_frauddetector.types.detector_version_status

        out["status"] = (
            aws_sdk_frauddetector.types.detector_version_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDetectorVersionResult:
    out: CreateDetectorVersionResult = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "detectorVersionId" in data:
        out["detector_version_id"] = data["detectorVersionId"]
    if "status" in data:
        import aws_sdk_frauddetector.types.detector_version_status

        out["status"] = (
            aws_sdk_frauddetector.types.detector_version_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
