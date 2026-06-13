"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAccountCustomPermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id


class DescribeAccountCustomPermissionRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account for which you want to describe the applied custom permissions profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountCustomPermissionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAccountCustomPermissionRequest:
    out: DescribeAccountCustomPermissionRequest = {}  # type: ignore[typeddict-item]
    return out
