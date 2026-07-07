"""Generated from Smithy shape ``com.amazonaws.rekognition#BlackFrame``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.max_pixel_threshold
    import aws_sdk_rekognition.types.min_coverage_percentage


class BlackFrame(TypedDict, closed=True):
    max_pixel_threshold: NotRequired[
        "aws_sdk_rekognition.types.max_pixel_threshold.MaxPixelThreshold"
    ]
    """<p> A threshold used to determine the maximum luminance value for a pixel to be considered black. In a full color range video, luminance values range from 0-255. A pixel value of 0 is pure black, and the most strict filter. The maximum black pixel value is computed as follows: max_black_pixel_value = minimum_luminance + MaxPixelThreshold *luminance_range. </p> <p>For example, for a full range video with BlackPixelThreshold = 0.1, max_black_pixel_value is 0 + 0.1 * (255-0) = 25.5.</p> <p>The default value of MaxPixelThreshold is 0.2, which maps to a max_black_pixel_value of 51 for a full range video. You can lower this threshold to be more strict on black levels.</p>"""
    min_coverage_percentage: NotRequired[
        "aws_sdk_rekognition.types.min_coverage_percentage.MinCoveragePercentage"
    ]
    """<p> The minimum percentage of pixels in a frame that need to have a luminance below the max_black_pixel_value for a frame to be considered a black frame. Luminance is calculated using the BT.709 matrix. </p> <p>The default value is 99, which means at least 99% of all pixels in the frame are black pixels as per the <code>MaxPixelThreshold</code> set. You can reduce this value to allow more noise on the black frame.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlackFrame) -> dict:
    out: dict = {}
    if "max_pixel_threshold" in value:
        out["MaxPixelThreshold"] = value["max_pixel_threshold"]
    if "min_coverage_percentage" in value:
        out["MinCoveragePercentage"] = value["min_coverage_percentage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BlackFrame:
    out: BlackFrame = {}  # type: ignore[typeddict-item]
    if "MaxPixelThreshold" in data:
        out["max_pixel_threshold"] = data["MaxPixelThreshold"]
    if "MinCoveragePercentage" in data:
        out["min_coverage_percentage"] = data["MinCoveragePercentage"]
    return out
