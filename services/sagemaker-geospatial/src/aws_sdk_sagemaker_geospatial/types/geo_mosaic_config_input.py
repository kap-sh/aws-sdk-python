"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GeoMosaicConfigInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.algorithm_name_geo_mosaic
    import aws_sdk_sagemaker_geospatial.types.string_list_input


class GeoMosaicConfigInput(TypedDict):
    algorithm_name: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.algorithm_name_geo_mosaic.AlgorithmNameGeoMosaic"
    ]
    """<p>The name of the algorithm being used for geomosaic.</p>"""
    target_bands: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.string_list_input.StringListInput"
    ]
    """<p>The target bands for geomosaic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoMosaicConfigInput) -> dict:
    out: dict = {}
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    if "target_bands" in value:
        import aws_sdk_sagemaker_geospatial.types.string_list_input

        out["TargetBands"] = (
            aws_sdk_sagemaker_geospatial.types.string_list_input.serialize_json(
                value["target_bands"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeoMosaicConfigInput:
    out: GeoMosaicConfigInput = {}  # type: ignore[typeddict-item]
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    if "TargetBands" in data:
        import aws_sdk_sagemaker_geospatial.types.string_list_input

        out["target_bands"] = (
            aws_sdk_sagemaker_geospatial.types.string_list_input.deserialize_json(
                data["TargetBands"]
            )
        )
    return out
