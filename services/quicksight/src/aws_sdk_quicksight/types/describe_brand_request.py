"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeBrandRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class DescribeBrandRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand.</p>"""
    brand_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the Quick brand.</p>"""
    version_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the specific version. The default value is the latest version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBrandRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBrandRequest:
    out: DescribeBrandRequest = {}  # type: ignore[typeddict-item]
    return out
