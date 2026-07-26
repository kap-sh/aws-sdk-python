"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#BandMathConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.custom_indices_input
    import capo_sagemaker_geospatial.types.string_list_input


class BandMathConfigInput(TypedDict, closed=True):
    predefined_indices: NotRequired[
        "capo_sagemaker_geospatial.types.string_list_input.StringListInput"
    ]
    """<p>One or many of the supported predefined indices to compute. Allowed values: <code>NDVI</code>, <code>EVI2</code>, <code>MSAVI</code>, <code>NDWI</code>, <code>NDMI</code>, <code>NDSI</code>, and <code>WDRVI</code>.</p>"""
    custom_indices: NotRequired[
        "capo_sagemaker_geospatial.types.custom_indices_input.CustomIndicesInput"
    ]
    """<p>CustomIndices that are computed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BandMathConfigInput) -> dict:
    out: dict = {}
    if "predefined_indices" in value:
        import capo_sagemaker_geospatial.types.string_list_input

        out["PredefinedIndices"] = (
            capo_sagemaker_geospatial.types.string_list_input.serialize_json(
                value["predefined_indices"]
            )
        )
    if "custom_indices" in value:
        import capo_sagemaker_geospatial.types.custom_indices_input

        out["CustomIndices"] = (
            capo_sagemaker_geospatial.types.custom_indices_input.serialize_json(
                value["custom_indices"]
            )
        )
    return out


def deserialize_json(data: dict) -> BandMathConfigInput:
    out: BandMathConfigInput = {}  # type: ignore[typeddict-item]
    if "PredefinedIndices" in data:
        import capo_sagemaker_geospatial.types.string_list_input

        out["predefined_indices"] = (
            capo_sagemaker_geospatial.types.string_list_input.deserialize_json(
                data["PredefinedIndices"]
            )
        )
    if "CustomIndices" in data:
        import capo_sagemaker_geospatial.types.custom_indices_input

        out["custom_indices"] = (
            capo_sagemaker_geospatial.types.custom_indices_input.deserialize_json(
                data["CustomIndices"]
            )
        )
    return out
