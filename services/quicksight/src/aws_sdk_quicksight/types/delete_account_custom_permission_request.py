"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteAccountCustomPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id


class DeleteAccountCustomPermissionRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account from which you want to unapply the custom permissions profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccountCustomPermissionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccountCustomPermissionRequest:
    out: DeleteAccountCustomPermissionRequest = {}  # type: ignore[typeddict-item]
    return out
