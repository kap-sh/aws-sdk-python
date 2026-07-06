"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetRasterDataCollectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.data_collection_arn


class GetRasterDataCollectionInput(TypedDict, closed=True):
    arn: "aws_sdk_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn"
    """<p>The Amazon Resource Name (ARN) of the raster data collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRasterDataCollectionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRasterDataCollectionInput:
    out: GetRasterDataCollectionInput = {}  # type: ignore[typeddict-item]
    return out
