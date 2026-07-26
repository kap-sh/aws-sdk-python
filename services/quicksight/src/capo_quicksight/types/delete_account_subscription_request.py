"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteAccountSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id


class DeleteAccountSubscriptionRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the account that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccountSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccountSubscriptionRequest:
    out: DeleteAccountSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
