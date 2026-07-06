"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeBrandAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id


class DescribeBrandAssignmentRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand assignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBrandAssignmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBrandAssignmentRequest:
    out: DescribeBrandAssignmentRequest = {}  # type: ignore[typeddict-item]
    return out
