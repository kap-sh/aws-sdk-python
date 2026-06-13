"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteDefaultQBusinessApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.namespace


class DeleteDefaultQBusinessApplicationRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Quick Sight account that you want to disconnect from a Amazon Q Business application.</p>"""
    namespace: NotRequired["aws_sdk_quicksight.types.namespace.Namespace"]
    """<p>The Quick Sight namespace that you want to delete a linked Amazon Q Business application from. If this field is left blank, the Amazon Q Business application is deleted from the default namespace. Currently, the default namespace is the only valid value for this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDefaultQBusinessApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDefaultQBusinessApplicationRequest:
    out: DeleteDefaultQBusinessApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
