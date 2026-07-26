"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteDefaultQBusinessApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace


class DeleteDefaultQBusinessApplicationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Quick Sight account that you want to disconnect from a Amazon Q Business application.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The Quick Sight namespace that you want to delete a linked Amazon Q Business application from. If this field is left blank, the Amazon Q Business application is deleted from the default namespace. Currently, the default namespace is the only valid value for this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDefaultQBusinessApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDefaultQBusinessApplicationRequest:
    out: DeleteDefaultQBusinessApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
