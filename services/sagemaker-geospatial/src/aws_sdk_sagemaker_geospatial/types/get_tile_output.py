"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetTileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.binary_file


class GetTileOutput(TypedDict, closed=True):
    binary_file: "aws_sdk_sagemaker_geospatial.types.binary_file.BinaryFile"
    """<p>The output binary file.</p>"""
