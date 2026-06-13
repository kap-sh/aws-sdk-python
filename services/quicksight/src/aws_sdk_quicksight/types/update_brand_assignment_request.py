"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateBrandAssignmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.aws_account_id


class UpdateBrandAssignmentRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand assignment.</p>"""
    brand_arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandAssignmentRequest) -> dict:
    out: dict = {}
    out["BrandArn"] = value["brand_arn"]
    return out


def deserialize_json(data: dict) -> UpdateBrandAssignmentRequest:
    out: UpdateBrandAssignmentRequest = {}  # type: ignore[typeddict-item]
    if "BrandArn" in data:
        out["brand_arn"] = data["BrandArn"]
    else:
        raise DeserializationError("UpdateBrandAssignmentRequest.brand_arn required")
    return out
