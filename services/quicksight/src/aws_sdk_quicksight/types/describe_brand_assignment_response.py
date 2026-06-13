"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeBrandAssignmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.string


class DescribeBrandAssignmentResponse(TypedDict):
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    brand_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBrandAssignmentResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "brand_arn" in value:
        out["BrandArn"] = value["brand_arn"]
    return out


def deserialize_json(data: dict) -> DescribeBrandAssignmentResponse:
    out: DescribeBrandAssignmentResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "BrandArn" in data:
        out["brand_arn"] = data["BrandArn"]
    return out
