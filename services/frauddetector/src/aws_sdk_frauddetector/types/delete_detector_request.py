"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteDetectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier


class DeleteDetectorRequest(TypedDict):
    detector_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The ID of the detector to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDetectorRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDetectorRequest:
    out: DeleteDetectorRequest = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError("DeleteDetectorRequest.detector_id required")
    return out
