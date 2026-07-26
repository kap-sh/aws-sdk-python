"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteBrandAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id


class DeleteBrandAssignmentRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand assignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrandAssignmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBrandAssignmentRequest:
    out: DeleteBrandAssignmentRequest = {}  # type: ignore[typeddict-item]
    return out
