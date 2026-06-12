"""Generated from Smithy shape ``com.amazonaws.frauddetector#DetectorVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.detector_version_status
    import aws_sdk_frauddetector.types.time
    import aws_sdk_frauddetector.types.whole_number_version_string


class DetectorVersionSummary(TypedDict):
    detector_version_id: NotRequired[
        "aws_sdk_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p>The detector version ID. </p>"""
    status: NotRequired[
        "aws_sdk_frauddetector.types.detector_version_status.DetectorVersionStatus"
    ]
    """<p>The detector version status. </p>"""
    description: NotRequired["aws_sdk_frauddetector.types.description.description"]
    """<p>The detector version description. </p>"""
    last_updated_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of when the detector version was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectorVersionSummary) -> dict:
    out: dict = {}
    if "detector_version_id" in value:
        out["detectorVersionId"] = value["detector_version_id"]
    if "status" in value:
        import aws_sdk_frauddetector.types.detector_version_status

        out["status"] = (
            aws_sdk_frauddetector.types.detector_version_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectorVersionSummary:
    out: DetectorVersionSummary = {}  # type: ignore[typeddict-item]
    if "detectorVersionId" in data:
        out["detector_version_id"] = data["detectorVersionId"]
    if "status" in data:
        import aws_sdk_frauddetector.types.detector_version_status

        out["status"] = (
            aws_sdk_frauddetector.types.detector_version_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    return out
