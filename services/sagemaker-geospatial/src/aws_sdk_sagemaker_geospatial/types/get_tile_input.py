"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetTileInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn
    import aws_sdk_sagemaker_geospatial.types.execution_role_arn
    import aws_sdk_sagemaker_geospatial.types.output_type
    import aws_sdk_sagemaker_geospatial.types.string_list_input
    import aws_sdk_sagemaker_geospatial.types.target_options


class GetTileInput(TypedDict):
    x: "int"
    """<p>The x coordinate of the tile input.</p>"""
    y: "int"
    """<p>The y coordinate of the tile input.</p>"""
    z: "int"
    """<p>The z coordinate of the tile input.</p>"""
    image_assets: "aws_sdk_sagemaker_geospatial.types.string_list_input.StringListInput"
    """<p>The particular assets or bands to tile.</p>"""
    target: "aws_sdk_sagemaker_geospatial.types.target_options.TargetOptions"
    """<p>Determines what part of the Earth Observation job to tile. 'INPUT' or 'OUTPUT' are the valid options.</p>"""
    arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    """<p>The Amazon Resource Name (ARN) of the tile operation.</p>"""
    image_mask: NotRequired["bool"]
    """<p>Determines whether or not to return a valid data mask.</p>"""
    output_format: NotRequired["str"]
    """<p>The data format of the output tile. The formats include .npy, .png and .jpg.</p>"""
    time_range_filter: NotRequired["str"]
    """<p>Time range filter applied to imagery to find the images to tile.</p>"""
    property_filters: NotRequired["str"]
    """<p>Property filters for the imagery to tile.</p>"""
    output_data_type: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.output_type.OutputType"
    ]
    """<p>The output data type of the tile operation.</p>"""
    execution_role_arn: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTileInput:
    out: GetTileInput = {}  # type: ignore[typeddict-item]
    return out
