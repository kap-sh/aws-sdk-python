"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeSpacePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.public_space_id


class DescribeSpacePermissionsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the space.</p>"""
    space_id: "aws_sdk_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space that you want to describe permissions for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSpacePermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSpacePermissionsRequest:
    out: DescribeSpacePermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
