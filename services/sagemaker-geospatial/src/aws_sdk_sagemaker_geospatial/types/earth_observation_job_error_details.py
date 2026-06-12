"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#EarthObservationJobErrorDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_error_type

class EarthObservationJobErrorDetails(TypedDict):
    type: NotRequired["aws_sdk_sagemaker_geospatial.types.earth_observation_job_error_type.EarthObservationJobErrorType"]
    """<p>The type of error in an Earth Observation job.</p>"""
    message: NotRequired["str"]
    """<p>A detailed message describing the error in an Earth Observation job.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EarthObservationJobErrorDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EarthObservationJobErrorDetails:
    out: EarthObservationJobErrorDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out