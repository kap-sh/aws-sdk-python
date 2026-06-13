"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeBrandPublishedVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class DescribeBrandPublishedVersionRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand.</p>"""
    brand_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the Quick brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBrandPublishedVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBrandPublishedVersionRequest:
    out: DescribeBrandPublishedVersionRequest = {}  # type: ignore[typeddict-item]
    return out
