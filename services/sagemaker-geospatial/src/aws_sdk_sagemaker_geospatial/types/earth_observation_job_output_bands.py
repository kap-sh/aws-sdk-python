"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#EarthObservationJobOutputBands``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.output_band

EarthObservationJobOutputBands: TypeAlias = list["aws_sdk_sagemaker_geospatial.types.output_band.OutputBand"]


# --- restJson1 ser/de ---
def serialize_json(value: EarthObservationJobOutputBands) -> list:
    import aws_sdk_sagemaker_geospatial.types.output_band
    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker_geospatial.types.output_band.serialize_json(item))
    return out


def deserialize_json(data: list) -> EarthObservationJobOutputBands:
    import aws_sdk_sagemaker_geospatial.types.output_band
    out: EarthObservationJobOutputBands = []
    for item in data:
        out.append(aws_sdk_sagemaker_geospatial.types.output_band.deserialize_json(item))
    return out