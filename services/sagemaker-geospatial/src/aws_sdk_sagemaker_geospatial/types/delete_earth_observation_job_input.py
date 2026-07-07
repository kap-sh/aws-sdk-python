"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#DeleteEarthObservationJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn


class DeleteEarthObservationJobInput(TypedDict, closed=True):
    arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    """<p>The Amazon Resource Name (ARN) of the Earth Observation job being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEarthObservationJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEarthObservationJobInput:
    out: DeleteEarthObservationJobInput = {}  # type: ignore[typeddict-item]
    return out
