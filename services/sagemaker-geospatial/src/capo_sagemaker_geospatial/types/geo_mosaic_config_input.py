"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GeoMosaicConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.algorithm_name_geo_mosaic
    import capo_sagemaker_geospatial.types.string_list_input


class GeoMosaicConfigInput(TypedDict, closed=True):
    algorithm_name: NotRequired[
        "capo_sagemaker_geospatial.types.algorithm_name_geo_mosaic.AlgorithmNameGeoMosaic"
    ]
    """<p>The name of the algorithm being used for geomosaic.</p>"""
    target_bands: NotRequired[
        "capo_sagemaker_geospatial.types.string_list_input.StringListInput"
    ]
    """<p>The target bands for geomosaic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoMosaicConfigInput) -> dict:
    out: dict = {}
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    if "target_bands" in value:
        import capo_sagemaker_geospatial.types.string_list_input

        out["TargetBands"] = (
            capo_sagemaker_geospatial.types.string_list_input.serialize_json(
                value["target_bands"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeoMosaicConfigInput:
    out: GeoMosaicConfigInput = {}  # type: ignore[typeddict-item]
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    if "TargetBands" in data:
        import capo_sagemaker_geospatial.types.string_list_input

        out["target_bands"] = (
            capo_sagemaker_geospatial.types.string_list_input.deserialize_json(
                data["TargetBands"]
            )
        )
    return out
