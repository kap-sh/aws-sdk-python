"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#EarthObservationJobList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output_config

EarthObservationJobList: TypeAlias = list["aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output_config.ListEarthObservationJobOutputConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: EarthObservationJobList) -> list:
    import aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output_config
    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> EarthObservationJobList:
    import aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output_config
    out: EarthObservationJobList = []
    for item in data:
        out.append(aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output_config.deserialize_json(item))
    return out