"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetTileOutput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.binary_file


class GetTileOutput(TypedDict):
    binary_file: "aws_sdk_sagemaker_geospatial.types.binary_file.BinaryFile"
    """<p>The output binary file.</p>"""
