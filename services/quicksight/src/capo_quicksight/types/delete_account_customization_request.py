"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteAccountCustomizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace


class DeleteAccountCustomizationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to delete Quick Sight customizations from.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The Quick Sight namespace that you're deleting the customizations from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccountCustomizationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccountCustomizationRequest:
    out: DeleteAccountCustomizationRequest = {}  # type: ignore[typeddict-item]
    return out
