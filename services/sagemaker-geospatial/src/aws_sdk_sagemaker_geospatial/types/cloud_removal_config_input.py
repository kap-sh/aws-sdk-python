"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#CloudRemovalConfigInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.algorithm_name_cloud_removal
    import aws_sdk_sagemaker_geospatial.types.string_list_input

class CloudRemovalConfigInput(TypedDict):
    algorithm_name: NotRequired["aws_sdk_sagemaker_geospatial.types.algorithm_name_cloud_removal.AlgorithmNameCloudRemoval"]
    """<p>The name of the algorithm used for cloud removal.</p>"""
    interpolation_value: NotRequired["str"]
    """<p>The interpolation value you provide for cloud removal.</p>"""
    target_bands: NotRequired["aws_sdk_sagemaker_geospatial.types.string_list_input.StringListInput"]
    """<p>TargetBands to be returned in the output of CloudRemoval operation.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CloudRemovalConfigInput) -> dict:
    out: dict = {}
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    if "interpolation_value" in value:
        out["InterpolationValue"] = value["interpolation_value"]
    if "target_bands" in value:
        import aws_sdk_sagemaker_geospatial.types.string_list_input
        out["TargetBands"] = aws_sdk_sagemaker_geospatial.types.string_list_input.serialize_json(value["target_bands"])
    return out


def deserialize_json(data: dict) -> CloudRemovalConfigInput:
    out: CloudRemovalConfigInput = {}  # type: ignore[typeddict-item]
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    if "InterpolationValue" in data:
        out["interpolation_value"] = data["InterpolationValue"]
    if "TargetBands" in data:
        import aws_sdk_sagemaker_geospatial.types.string_list_input
        out["target_bands"] = aws_sdk_sagemaker_geospatial.types.string_list_input.deserialize_json(data["TargetBands"])
    return out