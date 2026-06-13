"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StackConfigInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.output_resolution_stack_input
    import aws_sdk_sagemaker_geospatial.types.string_list_input


class StackConfigInput(TypedDict):
    output_resolution: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.output_resolution_stack_input.OutputResolutionStackInput"
    ]
    """<p>The structure representing output resolution (in target georeferenced units) of the result of stacking operation.</p>"""
    target_bands: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.string_list_input.StringListInput"
    ]
    """<p>A list of bands to be stacked in the specified order. When the parameter is not provided, all the available bands in the data collection are stacked in the alphabetical order of their asset names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StackConfigInput) -> dict:
    out: dict = {}
    if "output_resolution" in value:
        import aws_sdk_sagemaker_geospatial.types.output_resolution_stack_input

        out["OutputResolution"] = (
            aws_sdk_sagemaker_geospatial.types.output_resolution_stack_input.serialize_json(
                value["output_resolution"]
            )
        )
    if "target_bands" in value:
        import aws_sdk_sagemaker_geospatial.types.string_list_input

        out["TargetBands"] = (
            aws_sdk_sagemaker_geospatial.types.string_list_input.serialize_json(
                value["target_bands"]
            )
        )
    return out


def deserialize_json(data: dict) -> StackConfigInput:
    out: StackConfigInput = {}  # type: ignore[typeddict-item]
    if "OutputResolution" in data:
        import aws_sdk_sagemaker_geospatial.types.output_resolution_stack_input

        out["output_resolution"] = (
            aws_sdk_sagemaker_geospatial.types.output_resolution_stack_input.deserialize_json(
                data["OutputResolution"]
            )
        )
    if "TargetBands" in data:
        import aws_sdk_sagemaker_geospatial.types.string_list_input

        out["target_bands"] = (
            aws_sdk_sagemaker_geospatial.types.string_list_input.deserialize_json(
                data["TargetBands"]
            )
        )
    return out
