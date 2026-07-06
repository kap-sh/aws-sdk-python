"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeCustomPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.custom_permissions_name


class DescribeCustomPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the custom permissions profile that you want described.</p>"""
    custom_permissions_name: (
        "aws_sdk_quicksight.types.custom_permissions_name.CustomPermissionsName"
    )
    """<p>The name of the custom permissions profile to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCustomPermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCustomPermissionsRequest:
    out: DescribeCustomPermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
