"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StopEarthObservationJobInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn


class StopEarthObservationJobInput(TypedDict):
    arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    """<p>The Amazon Resource Name (ARN) of the Earth Observation job being stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopEarthObservationJobInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> StopEarthObservationJobInput:
    out: StopEarthObservationJobInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("StopEarthObservationJobInput.arn required")
    return out
