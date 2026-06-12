"""Generated from Smithy shape ``com.amazonaws.frauddetector#DescribeDetectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.detector_version_max_results
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.string


class DescribeDetectorRequest(TypedDict):
    detector_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The detector ID.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next token from the previous response.</p>"""
    max_results: NotRequired[
        "aws_sdk_frauddetector.types.detector_version_max_results.DetectorVersionMaxResults"
    ]
    """<p>The maximum number of results to return for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDetectorRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDetectorRequest:
    out: DescribeDetectorRequest = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError("DescribeDetectorRequest.detector_id required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
