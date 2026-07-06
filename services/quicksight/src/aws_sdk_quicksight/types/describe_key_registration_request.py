"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeKeyRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.boolean


class DescribeKeyRegistrationRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the customer managed key registration that you want to describe.</p>"""
    default_key_only: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>Determines whether the request returns the default key only.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeKeyRegistrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeKeyRegistrationRequest:
    out: DescribeKeyRegistrationRequest = {}  # type: ignore[typeddict-item]
    return out
