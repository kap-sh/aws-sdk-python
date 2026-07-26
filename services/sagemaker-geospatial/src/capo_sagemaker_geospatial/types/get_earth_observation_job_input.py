"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetEarthObservationJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.earth_observation_job_arn


class GetEarthObservationJobInput(TypedDict, closed=True):
    arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    """<p>The Amazon Resource Name (ARN) of the Earth Observation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEarthObservationJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEarthObservationJobInput:
    out: GetEarthObservationJobInput = {}  # type: ignore[typeddict-item]
    return out
