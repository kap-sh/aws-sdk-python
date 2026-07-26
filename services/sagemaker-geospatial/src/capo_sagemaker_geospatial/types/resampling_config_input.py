"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ResamplingConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.algorithm_name_resampling
    import capo_sagemaker_geospatial.types.output_resolution_resampling_input
    import capo_sagemaker_geospatial.types.string_list_input


class ResamplingConfigInput(TypedDict, closed=True):
    output_resolution: "capo_sagemaker_geospatial.types.output_resolution_resampling_input.OutputResolutionResamplingInput"
    """<p>The structure representing output resolution (in target georeferenced units) of the result of resampling operation.</p>"""
    algorithm_name: NotRequired[
        "capo_sagemaker_geospatial.types.algorithm_name_resampling.AlgorithmNameResampling"
    ]
    """<p>The name of the algorithm used for resampling.</p>"""
    target_bands: NotRequired[
        "capo_sagemaker_geospatial.types.string_list_input.StringListInput"
    ]
    """<p>Bands used in the operation. If no target bands are specified, it uses all bands available in the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResamplingConfigInput) -> dict:
    out: dict = {}
    import capo_sagemaker_geospatial.types.output_resolution_resampling_input

    out["OutputResolution"] = (
        capo_sagemaker_geospatial.types.output_resolution_resampling_input.serialize_json(
            value["output_resolution"]
        )
    )
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


def deserialize_json(data: dict) -> ResamplingConfigInput:
    out: ResamplingConfigInput = {}  # type: ignore[typeddict-item]
    if "OutputResolution" in data:
        import capo_sagemaker_geospatial.types.output_resolution_resampling_input

        out["output_resolution"] = (
            capo_sagemaker_geospatial.types.output_resolution_resampling_input.deserialize_json(
                data["OutputResolution"]
            )
        )
    else:
        raise DeserializationError("ResamplingConfigInput.output_resolution required")
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
